.PHONY: up, down, clean

up:
	docker compose up -d --build

down:
	docker compose down --volumes

start:
	docker compose start

stop:
	docker compose stop

restart:
	docker compose restart

logs:
	docker compose logs -f

install_sshd:
	docker exec postgres_db bash -c "apt-get update && apt-get install -y openssh-server"

incr:

full:

diff:
