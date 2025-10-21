FROM ubuntu:latest
LABEL authors="juanjo"

FROM python:3.11-slim

WORKDIR /server

COPY app /server/app
COPY .env /server/.env
COPY run.py /server/run.py

RUN pip install --upgrade pip
RUN pip install --no-cache-dir fastapi uvicorn python-dotenv

CMD ["python", "run.py"]