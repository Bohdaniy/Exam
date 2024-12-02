
FROM python:3.10-alpine
RUN apk add --update python3 py3-pip
RUN pip install --upgrade pip setuptools
WORKDIR /app
COPY . /app
CMD ["python3", "main.py"]
