FROM python:3.13.3-slim

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 80

ENTRYPOINT ["python" , "app.py"]