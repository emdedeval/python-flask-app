FROM python:3.14.0a3-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 80

ENTRYPOINT ["python" , "app.py"]