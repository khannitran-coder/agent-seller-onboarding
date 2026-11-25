# Relations — SIM-BATCH-002 r1

Quan hệ do Claude đề xuất, người duyệt xác nhận. Định dạng `batch_id:client_record_id`; tham chiếu SIM-BATCH-001 là chéo batch.

| Từ | Loại | Đến |
|---|---|---|
| c0001 | depends_on | SIM-BATCH-001:c0006 |
| c0002 | depends_on | SIM-BATCH-001:c0001 |
| c0003 | depends_on | SIM-BATCH-001:c0011 |
| c0004 | depends_on | SIM-BATCH-001:c0001 |
| c0006 | depends_on | SIM-BATCH-001:c0018 |
| c0007 | depends_on | SIM-BATCH-002:c0009 |
| c0008 | depends_on | SIM-BATCH-001:c0019 |
| c0008 | depends_on | SIM-BATCH-002:c0009 |
| c0009 | depends_on | SIM-BATCH-002:c0011 |
| c0010 | depends_on | SIM-BATCH-001:c0004 |
| c0011 | depends_on | SIM-BATCH-001:c0007 |
| c0012 | depends_on | SIM-BATCH-002:c0009 |
| c0012 | depends_on | SIM-BATCH-001:c0009 |
| c0013 | depends_on | SIM-BATCH-001:c0012 |

Không có `supersedes`: chưa có KU canonical.
