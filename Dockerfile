FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Запуск сервера с указанием полного пути к manage.py
CMD ["python", "myproject/manage.py", "runserver", "0.0.0.0:8000"]
