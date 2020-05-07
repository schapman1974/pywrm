# Docerfile to build PyWRM with dxh and w2ui support
FROM python3.8:latest

COPY requirements.txt .

RUN ["pip", "install", "-r", "requirements.txt"]

ADD . /PyWRM

WORKDIR /PyWRM

ENTRYPOINT ["python", "main.py"]