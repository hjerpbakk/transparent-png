FROM python:slim-buster

COPY . /app
WORKDIR /app

RUN pip install Pillow

RUN mkdir image
ENTRYPOINT ["sh", "-c", "cd ./image && python ../transparent_png.py \"$@\"", "--"]