
ALTER SYSTEM SET archive_mode = on;
ALTER SYSTEM SET archive_log_format = '%t_%s_%r.arc';
ALTER SYSTEM SET max_wal_senders = 10;
ALTER SYSTEM SET wal_level = replica;
ALTER SYSTEM SET archive_command = 'pgbackrest --stanza=demo archive-push %p';
ALTER SYSTEM SET restore_command = 'pgbackrest --stanza=main archive-get %f "%p"';
SELECT pg_reload_conf();
