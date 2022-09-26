FROM python:3.10-slim 
# python:3.9

WORKDIR /usr/src/app

RUN apt-get update -y && apt-get install -y python3-pip python3-dev 

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

ENV APP_PORT=8080
ENV APP_RELOAD=True
ENV APP_WORKERS=2


CMD ["python3", "./main.py"]
