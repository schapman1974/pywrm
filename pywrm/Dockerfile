# Dockerfile to build PyWRM with dxh and w2ui support
FROM python:3.8 as base

WORKDIR /PyWRM

COPY requirements.txt /PyWRM

RUN ["pip", "install", "-r", "requirements.txt"]

RUN apt-get update && apt-get -y install git

ADD . /PyWRM

# get specific commit of dhx javascript
WORKDIR /
RUN git clone https://github.com/schapman1974/dhtmlx-suite-gpl.git /dhx
WORKDIR /dhx
RUN git checkout d27decd40b8bbe83a02da198e0e1b8787b057bbc
#COPY --from=build1 /dhx/codebase /PyWRM/static/codebase

# get specific commit of w2ui javascript
WORKDIR /
RUN git clone https://github.com/vitmalina/w2ui.git /w2uisrc
WORKDIR /w2uisrc
RUN git checkout 78d7229ea1915ccee677d5cce300e340aadc1bcf

# copy both libraries to static folder
COPY --from=base /dhx/codebase /PyWRM/static/codebase
COPY --from=base /w2uisrc/dist /PyWRM/static/w2ui

WORKDIR /PyWRM

EXPOSE 8090

ENTRYPOINT ["python", "main.py"]
