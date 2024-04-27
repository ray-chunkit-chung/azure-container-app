FROM unit:1.32.1-python3.11

# Include model in the image
ADD https://publicraychung.blob.core.windows.net/text-classifier/models--oshizo--japanese-sexual-moderation-v2.tar.gz /build/huggingface/models--oshizo--japanese-sexual-moderation-v2.tar.gz
RUN tar -xzvf /build/huggingface/models--oshizo--japanese-sexual-moderation-v2.tar.gz -C /build/huggingface/ \
    && rm /build/huggingface/models--oshizo--japanese-sexual-moderation-v2.tar.gz

# Unit entrypoint config
COPY ./config/config.json /docker-entrypoint.d/config.json

# Install Python and dependencies
COPY requirements.txt /build/requirements.txt
RUN apt update && apt install -y python3-pip                                 \
    && pip3 install -r /build/requirements.txt                               \
    && apt remove -y python3-pip                                             \
    && apt autoremove --purge -y                                             \
    && rm -rf /var/lib/apt/lists/* /etc/apt/sources.list.d/*.list

# Include app
COPY . /build

EXPOSE 80


