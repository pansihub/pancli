FROM python:3.8.1-alpine3.11

RUN apk add libffi-dev \
    openssl-dev gcc libc-dev make libxml2-dev libxslt-dev \
    tzdata jpeg-dev zlib-dev freetype-dev lcms2-dev openjpeg-dev tiff-dev tk-dev tcl-dev
ADD . /app_src
WORKDIR /app_src
RUN pip install -r requirements.txt
RUN python /app_src/setup.py install
RUN pip install scrapy
WORKDIR /app
ENV TZ /usr/share/zoneinfo/Etc/UTC
CMD ["pansi"]