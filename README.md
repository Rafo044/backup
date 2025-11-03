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
