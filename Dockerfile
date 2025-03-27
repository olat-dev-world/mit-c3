# syntax=docker/dockerfile:1

FROM python:3.12

RUN pip install flask

WORKDIR /mit-c3
COPY . .

CMD ["python3"]
EXPOSE 3000