FROM python:2.7

CMD mkdir -p /usr/src/app/p1
WORKDIR /usr/src/app/p1

COPY requirements.txt requirements.txt


RUN pip install -r requirements.txt

COPY . .

CMD python main.py


