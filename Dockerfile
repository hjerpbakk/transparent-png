FROM python:3.7-alpine

ENV LIBRARY_PATH=/lib:/usr/lib \
    PNGOUT_VERSION=20150319

COPY . /app
WORKDIR /app

# For pip
RUN apk update && apk add \
    build-base python-dev py-pip jpeg-dev zlib-dev curl \
    # For PNGOUT
    && curl -O http://static.jonof.id.au/dl/kenutils/pngout-$PNGOUT_VERSION-linux-static.tar.gz \
    && tar zxf pngout-$PNGOUT_VERSION-linux-static.tar.gz \
    && cd pngout-$PNGOUT_VERSION-linux-static \
    && cp -f x86_64/pngout-static /usr/local/bin/pngout \
    && cd ..

RUN pip install Pillow

RUN mkdir image
ENTRYPOINT ["sh", "-c", "cd ./image && python ../transparent_png.py \"$@\"", "--"]