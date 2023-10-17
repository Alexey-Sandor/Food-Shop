FROM python:3.11-slim

WORKDIR /app

COPY . /app/

RUN pip3 install -r /app/requirements.txt --no-cache-dir


CMD ["gunicorn", "food_shop.wsgi:application", "--bind", "0:8000" ] 
