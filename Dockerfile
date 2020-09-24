FROM python:3.8-buster

RUN apt update && apt-get update && apt install libffi-dev firefox-esr python3-twisted --fix-missing -y

RUN export GECKO_DRIVER_VERSION='v0.24.0' && \
    wget https://github.com/mozilla/geckodriver/releases/download/$GECKO_DRIVER_VERSION/geckodriver-$GECKO_DRIVER_VERSION-linux64.tar.gz && \
    tar -xvzf geckodriver-$GECKO_DRIVER_VERSION-linux64.tar.gz && \
    rm geckodriver-$GECKO_DRIVER_VERSION-linux64.tar.gz && \
    chmod +x geckodriver && \
    cp -f geckodriver /usr/local/bin/

# RUN apt install libffi-dev \
#     openssl-dev gcc libc-dev make libxml2-dev libxslt-dev \
#     tzdata jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev
ADD . /app_src
WORKDIR /app_src
RUN pip install -r requirements.txt
RUN python /app_src/setup.py install
RUN pip install scrapy
WORKDIR /app
ENV TZ /usr/share/zoneinfo/Etc/UTC
CMD ["pansi"]