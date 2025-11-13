# PgBackup-Ansible - Backup Prosesi

Bu qovluq PostgreSQL verilənlər bazalarının avtomatlaşdırılmış backup və bərpa proseslərini idarə etmək üçün Ansible playbooklarını ehtiva edir. pgBackRest istifadə olunaraq tam (full), inkremental (incremental) və differensial (differential) backup strategiyaları tətbiq edilir.

## Backup Növləri

*   **Full Backup**: Verilənlər bazasının tam surətini yaradır. Bərpa üçün tək başına istifadə edilə bilər.
*   **Incremental Backup**: Sonuncu tam və ya inkremental backupdan bəri dəyişən məlumatların surətini yaradır.
*   **Differential Backup**: Sonuncu tam backupdan bəri dəyişən məlumatların surətini yaradır.

## RPO (Recovery Point Objective) və RTO (Recovery Time Objective)

pgBackRest tərəfindən yaradılan `pgbackrest_info.json` faylı RPO və RTO-nun hesablanması üçün kritik məlumatları ehtiva edir.

*   **RPO Hesablanması**: Son uğurlu backupın bitmə zamanı ilə indiki vaxt arasındakı fərq RPO-nu göstərir. Bu, itirilə biləcək maksimal məlumat yaşını müəyyənləşdirir. WAL arxivləri sayəsində PITR (Point-in-Time Recovery) imkanı RPO-nu sıfıra yaxınlaşdıra bilər.

*   **RTO Hesablanması**: Fəlakətdən sonra sistemin normal işlək vəziyyətinə qayıtması üçün icazə verilən maksimal müddətdir. pgBackRest `info` faylı backupın özünün nə qədər vaxt apardığını göstərir ki, bu da RTO-nun bir komponentidir. Ümumi RTO həmçinin serverin hazırlanması, proqram təminatının quraşdırılması və test müddətlərini də əhatə edir.

## Əlavə Məlumat

pgBackRest haqqında ətraflı məlumat və Ansible playbooklarının istifadə qaydaları layihənin əsas `README.md` və `docs/index.md` fayllarında mövcuddur.

Aşağıdakı şəkil, backup hesabatının nümunə skrinşotudur:

![Backup Report](./report.png)