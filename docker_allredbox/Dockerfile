#FROM ubuntu:20.04
FROM debian:stable-slim 

RUN apt-get update && \
    apt-get install \
        build-essential \
        curl \
        file \
        git \
        ruby-full \
        locales \
        --no-install-recommends -y && \
    rm -rf /var/lib/apt/lists/*

RUN localedef -i en_US -f UTF-8 en_US.UTF-8

RUN useradd -m -s /bin/bash linuxbrew && \
    echo 'linuxbrew ALL=(ALL) NOPASSWD:ALL' >>/etc/sudoers

RUN useradd -m -s /bin/bash mallred && \
    echo 'mallred ALL=(ALL) NOPASSWD:ALL' >>/etc/sudoers

USER linuxbrew
#USER mallred
RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/Linuxbrew/install/master/install.sh)"

USER root
ENV PATH="/home/linuxbrew/.linuxbrew/bin:${PATH}"
RUN chown -R mallred: /home/linuxbrew/.linuxbrew

USER mallred
ENV PATH="/home/linuxbrew/.linuxbrew/bin:${PATH}"
RUN brew install \
    figlet \
    htop \
    httpie \
    jp2a \
    jq \
    nmap \
    vim \
    watch \
    wget
