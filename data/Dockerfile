FROM postgres:18

RUN apt-get update && \
    apt-get install -y openssh-server && \
    mkdir -p /var/run/sshd

RUN echo 'root:postgres' | chpasswd && \
    sed -i 's/#PermitRootLogin prohibit-password/PermitRootLogin yes/' /etc/ssh/sshd_config

RUN apt-get install -y python3-pip python3-dev build-essential


EXPOSE 22

CMD service ssh start && docker-entrypoint.sh postgres
