FROM python:3.9-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл с зависимостями
COPY requirements.txt requirements.txt

RUN pip install --no-cache-dir -r requirements.txt

# Копируем приложение
COPY python.py python.py

EXPOSE 5000

# Указываем команду для запуска приложения
CMD ["python", "python.py"]
