# Учебное окружение для лабораторных работ курса «Основы Linux».
# База — Ubuntu 22.04 LTS (совпадает с дистрибутивом, на который ориентировано пособие).

FROM ubuntu:22.04

# Не задавать вопросы во время установки пакетов.
ENV DEBIAN_FRONTEND=noninteractive

# Базовый набор инструментов, которые используются в лабораторных работах.
RUN apt-get update && apt-get install -y --no-install-recommends \
    sudo \
    ca-certificates \
    man-db \
    less \
    nano \
    vim \
    tree \
    file \
    coreutils \
    findutils \
    grep \
    sed \
    gawk \
    tar \
    gzip \
    bzip2 \
    xz-utils \
    rsync \
    iproute2 \
    iputils-ping \
    dnsutils \
    traceroute \
    net-tools \
    curl \
    wget \
    openssh-client \
    git \
    cron \
    python3 \
    python3-venv \
    python3-pip \
    htop \
    procps \
 && rm -rf /var/lib/apt/lists/*

# Учебная запись student с правами sudo без пароля (среда одноразовая и изолированная).
RUN useradd -m -s /bin/bash student \
 && echo "student ALL=(ALL) NOPASSWD:ALL" > /etc/sudoers.d/student \
 && chmod 0440 /etc/sudoers.d/student

USER student
WORKDIR /home/student

CMD ["/bin/bash"]
