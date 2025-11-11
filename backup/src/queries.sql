
ALTER SYSTEM SET max_wal_senders = 10;
ALTER SYSTEM SET wal_level = replica;
ALTER SYSTEM SET archive_command = '/usr/bin/pgbackrest --stanza=netflix_shows archive-push %p';
ALTER SYSTEM SET restore_command = '/usr/bin/pgbackrest --stanza=netflix_shows archive-get %f "%p"';
ALTER SYSTEM SET archive_timeout = '120s';
ALTER SYSTEM SET archive_mode = on;
SELECT pg_reload_conf();
