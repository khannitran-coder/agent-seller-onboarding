# Tác giả: PM - TKC. BẢN NHÁP, không dùng trước D-08b. Chỉ Windows có Excel.
param(
    [Parameter(Mandatory=$true)][string]$InputFile,
    [Parameter(Mandatory=$true)][string]$OutputFile,
    [string]$SheetName = 'Bang_Gia',
    [int]$ProductColumn = 2
)
$ErrorActionPreference = 'Stop'
$source = [IO.Path]::GetFullPath($InputFile)
$output = [IO.Path]::GetFullPath($OutputFile)
if (-not (Test-Path -LiteralPath $source -PathType Leaf)) { throw 'Thiếu Excel' }
if (Test-Path -LiteralPath $output) { throw 'Không ghi đè đầu ra' }
if ([IO.Path]::GetExtension($source) -ne '.xlsx' -or [IO.Path]::GetExtension($output) -ne '.pdf') { throw 'Định dạng không hợp lệ' }
if ($ProductColumn -lt 1) { throw 'Cột sản phẩm không hợp lệ' }
New-Item -ItemType Directory -Force -Path ([IO.Path]::GetDirectoryName($output)) | Out-Null
$x = $null; $wb = $null
try {
    $x = New-Object -ComObject Excel.Application
    $x.Visible = $false; $x.DisplayAlerts = $false; $x.AutomationSecurity = 3
    # Chỉ đọc, không cập nhật link ngoài; workbook nguồn không bị lưu.
    $wb = $x.Workbooks.Open($source, 0, $true)
    $ws = $wb.Worksheets.Item($SheetName)
    $last = $ws.Cells($ws.Rows.Count, $ProductColumn).End(-4162).Row
    while ($last -gt 1 -and -not "$($ws.Cells($last, $ProductColumn).Text)".Trim()) { $last-- }
    if ($last -le 1) { throw 'Không có dòng sản phẩm' }
    $lastCol = $ws.UsedRange.Column + $ws.UsedRange.Columns.Count - 1
    $ws.PageSetup.PrintArea = $ws.Range($ws.Cells(1,1), $ws.Cells($last,$lastCol)).Address()
    $ws.PageSetup.Orientation = 2
    $ws.PageSetup.Zoom = $false
    $ws.PageSetup.FitToPagesWide = 1
    $ws.PageSetup.FitToPagesTall = $false
    $ws.ExportAsFixedFormat(0, $output)
    Write-Output "Đã xuất bản sao PDF tới dòng $last; người kiểm số trang và vùng in"
} catch {
    Remove-Item -LiteralPath $output -Force -ErrorAction SilentlyContinue
    throw 'Chưa xác minh bản xuất Excel PDF'
} finally {
    if ($wb) { $wb.Close($false) }
    if ($x) { $x.Quit() }
}
