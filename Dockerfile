# Этап 1: Соберите HTML документацию
FROM python:3.8 as builder

# Переменная окружения PYTHONUNBUFFERED, чтобы вывод был немедленно показан в консоли
ENV PYTHONUNBUFFERED=1

# Установка системных зависимостей (graphviz и Java Runtime Environment)
RUN apt-get update && apt-get install -y graphviz default-jre

WORKDIR /app
COPY . /app

# Копируем plantuml.jar в контейнер
COPY plantuml.jar /app/plantuml.jar

# Установите зависимости из файла requirements.txt и перенаправьте вывод в stdout (параметр 2>&1)
RUN pip install --no-cache-dir -r requirements.txt -v 2>&1

# Соберите HTML документацию и перенаправьте вывод в stdout (параметр 2>&1)
RUN make html 2>&1

# Копируем сгенерированную документацию в отдельную директорию
RUN mkdir /app/temp_html
RUN cp -r /app/build/html /app/temp_html/

# Этап 2: Настройка веб-сервера
# FROM nginx:alpine

# Копирование собранной документации из временной папки в контейнер Nginx
# COPY --from=builder /app/temp_html/build/html /usr/share/nginx/html

# Указываем порт для доступа к веб-серверу
# EXPOSE 80

# Запускаем Nginx
CMD ["nginx", "-g", "daemon off;"]
