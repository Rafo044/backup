# Backup prosesi əsasən 3 növü var :
1. Full Backup
2. Incremental Backup
3. Differential Backup

Bu backupları recovery edəndə aşagıdakı kimi etmək olur:
1. Point-in-Time Recovery (PITR)

# RTO (Recovery Time Objective)

RTO çox daha rəsmi və universal bir termindir:
Tərifi: Fəlakət baş verdikdən sonra sistemin işlək vəziyyətə qayıtması üçün icazə verilən maksimal vaxt.
Məqsəd: Service Level Agreement (SLA) və disaster recovery planları üçün kritikdir.
PostgreSQL-də təsiri:
Backup və bərpa strategiyasını müəyyənləşdirir.
Məsələn, 1 saatlıq RTO varsa, database bərpa proseduru 1 saatdan çox sürməməlidir.
PostgreSQL nümunəsi:
Base backup + WAL archiving:
Base backup alınır, WAL faylları saxlanılır.
Fəlakət zamanı:
Base backup bərpa olunur
WAL faylları replay edilir
Database əvvəlki son vəziyyətinə gətirilir
RTO burada base backup bərpa vaxtı + WAL replay vaxtıdır.
PgBackRest və Barman kimi backup həllərində RTO və RPO (Recovery Point Objective – itirilə biləcək data miqdarı) öncədən planlanır.


|Tapşırıqın adı |Ansible Tag|Gördüyü iş|Komanda|
| --- | --- | --- | --- |
| Full Backup | create_full_backup | Full bərpanın alınması |  |
| Incremental Backup | create_incremental_backup | Incremental bərpanın alınması |  |
| Differential Backup | create_differential_backup | Differential bərpanın alınması |  |
| Point-in-Time Recovery | create_point_in_time_recovery | Hər hansı zamana görə bərpa prosesi |  |
| Install pgbackrest | install_pgbackrest | pgbackrest-in yüklənməsi |  |
| Install wget | install_wget | wget-in yüklənməsi |  |
| Queries skripti | execute_sql_script_queries | Queries skriptinin postgresə yüklənməsi |  |
| Flight skripti | execute_sql_script_flight | Flight skriptinin postgresə yüklənməsi |  |
| Install Flight dataset | install_flight_dataset | Flight datasetinin mənbədən yüklənməsi |  |
