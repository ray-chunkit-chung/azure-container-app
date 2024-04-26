FROM nginx/unit:1.32.1-python3.11

COPY ./config/config.json /docker-entrypoint.d/config.json

COPY requirements.txt /build/requirements.txt

RUN apt update && apt install -y python3-pip                                  \
    && pip3 install -r /build/requirements.txt                               \
    && apt remove -y python3-pip                                              \
    && apt autoremove --purge -y                                              \
    && rm -rf /var/lib/apt/lists/* /etc/apt/sources.list.d/*.list

COPY . /build

EXPOSE 80
