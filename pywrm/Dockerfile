# Dockerfile to build PyWRM with dxh and w2ui support
FROM python:3.8 as intermediate

WORKDIR /PyWRM

COPY requirements.txt /PyWRM

RUN ["pip", "install", "-r", "requirements.txt"]

RUN apt-get update && apt-get -y install git

ADD . /PyWRM

# get specific commit of dhx javascript
FROM intermediate as build1
WORKDIR /
RUN git clone https://github.com/schapman1974/dhtmlx-suite-gpl.git /dhx
WORKDIR /dhx
RUN git checkout d27decd40b8bbe83a02da198e0e1b8787b057bbc
COPY --from=build1 /dhx/codebase /PyWRM/static/codebase

# get specific commit of dhx javascript
FROM build1 as build2
WORKDIR /
RUN git clone https://github.com/vitmalina/w2ui.git /w2uisrc
WORKDIR /w2uisrc
RUN git checkout 78d7229ea1915ccee677d5cce300e340aadc1bcf
COPY --from=build2 /w2uisrc/dist /PyWRM/static/w2ui

WORKDIR /PyWRM

RUN ls -ltr static

ENTRYPOINT ["python", "main.py"]