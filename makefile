.PHONY: up, down, clean

up:
	docker compose up -d --build

down:
	docker compose down --volumes

install_sshd:
	docker exec postgres_db bash -c "apt-get update && apt-get install -y openssh-server"

incr:

full:

diff:
