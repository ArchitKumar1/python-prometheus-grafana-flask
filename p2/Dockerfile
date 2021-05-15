FROM python:2.7

CMD mkdir -p /usr/src/app/p2
WORKDIR /usr/src/app/p2

COPY requirements.txt requirements.txt


RUN pip install -r requirements.txt

COPY . .

CMD python main.py



