# syntax=docker/dockerfile:1

FROM python:3.11.7

WORKDIR /recipe-box-2

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

EXPOSE 5000

COPY . .

ENV FLASK_APP=app.py

CMD [ "python3", "app.py", "---debug"]