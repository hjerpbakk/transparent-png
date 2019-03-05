FROM python:3.7-alpine
COPY . /app
WORKDIR /app
RUN apk add build-base python-dev py-pip jpeg-dev zlib-dev
ENV LIBRARY_PATH=/lib:/usr/lib
RUN pip install Pillow
RUN mkdir image
ENTRYPOINT ["sh", "-c", "cd ./image && python ../transparent_png.py \"$@\"", "--"]