FROM python:3.6-alpine
COPY . /app
WORKDIR /app
RUN apk add build-base python-dev py-pip jpeg-dev zlib-dev
ENV LIBRARY_PATH=/lib:/usr/lib
RUN pip install Pillow
ENTRYPOINT ["python", "transparent_png.py"]