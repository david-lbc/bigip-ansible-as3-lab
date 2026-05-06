FROM rundeck/rundeck:5.20.0

USER root

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        ca-certificates \
        git \
        python3 \
        python3-pip \
        python3-venv \
        sshpass \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt /tmp/lab-requirements.txt
RUN python3 -m pip install --break-system-packages -r /tmp/lab-requirements.txt

COPY collections/requirements.yml /tmp/collections-requirements.yml
RUN mkdir -p /opt/ansible/collections \
    && ansible-galaxy collection install -r /tmp/collections-requirements.yml -p /opt/ansible/collections

ENV ANSIBLE_COLLECTIONS_PATH=/home/rundeck/lab/collections:/opt/ansible/collections:/home/rundeck/.ansible/collections
ENV ANSIBLE_FORCE_COLOR=true

USER rundeck
WORKDIR /home/rundeck/lab
