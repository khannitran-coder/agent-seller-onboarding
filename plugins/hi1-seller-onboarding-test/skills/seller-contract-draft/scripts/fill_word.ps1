# Tác giả: PM - TKC. BẢN NHÁP, không dùng trước D-08b. Chỉ Windows có Word.
param([Parameter(Mandatory=$true)][string]$Config)
$ErrorActionPreference = 'Stop'
$c = Get-Content -Raw -Encoding UTF8 $Config | ConvertFrom-Json
$source = [IO.Path]::GetFullPath($c.source)
$output = [IO.Path]::GetFullPath($c.output)
if ($source -eq $output -or (Test-Path -LiteralPath $output)) { throw 'Đầu ra phải là bản sao mới' }
if ([IO.Path]::GetExtension($source) -ne '.docx' -or [IO.Path]::GetExtension($output) -ne '.docx') { throw 'Chỉ hỗ trợ docx' }
if (-not (Test-Path -LiteralPath $source -PathType Leaf)) { throw 'Thiếu mẫu' }
if (-not $c.pairs -or $c.pairs.Count -eq 0) { throw 'Thiếu cặp thay' }
$pdf = [IO.Path]::ChangeExtension($output, '.pdf')
if (Test-Path -LiteralPath $pdf) { throw 'PDF đầu ra đã tồn tại' }
New-Item -ItemType Directory -Force -Path ([IO.Path]::GetDirectoryName($output)) | Out-Null
$w = $null; $d = $null; $made = $false
try {
    Copy-Item -LiteralPath $source -Destination $output
    $made = $true
    $w = New-Object -ComObject Word.Application
    $w.Visible = $false
    $w.AutomationSecurity = 3
    $d = $w.Documents.Open($output)
    foreach ($pair in $c.pairs) {
        if ($pair.Count -ne 2 -or [string]::IsNullOrEmpty($pair[0]) -or $pair[0] -eq $pair[1]) { throw 'Cặp thay không hợp lệ' }
        $count = 0
        $range = $d.Content
        $find = $range.Find
        $find.ClearFormatting()
        $find.MatchCase = $true
        $find.MatchWildcards = $false
        $find.Wrap = 0
        while ($find.Execute([string]$pair[0])) {
            $range.Text = [string]$pair[1]
            $count++
            $range.Collapse(0)
        }
        # Không in giá trị cặp thay, chỉ số lần.
        Write-Output "Số chỗ thay: $count"
        if ($count -eq 0) { throw 'Không tìm thấy chuỗi cần thay; dừng' }
    }
    $d.Save()
    $d.ExportAsFixedFormat($pdf, 17)
    $d.Close(0); $d = $null
    Write-Output 'Đã tạo bản nháp; người kiểm toàn bộ nội dung và PDF'
} catch {
    if ($d) { $d.Close(0); $d = $null }
    if ($made) { Remove-Item -LiteralPath $output -Force -ErrorAction SilentlyContinue }
    Remove-Item -LiteralPath $pdf -Force -ErrorAction SilentlyContinue
    throw 'Lỗi ghép Word; chưa có bản nháp hoàn tất'
} finally {
    if ($d) { $d.Close(0) }
    if ($w) { $w.Quit() }
}
