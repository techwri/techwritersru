# Этап 1: Соберите HTML документацию
FROM python:3.8 as builder

WORKDIR /app
COPY . /app

# Установите зависимости из файла requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


# Соберите HTML документацию
RUN make html

# Этап 2: Настройка веб-сервера
FROM nginx:alpine

# Копирование собранной документации в контейнер Nginx
COPY --from=builder /app/build/html /usr/share/nginx/html

# Указываем порт для доступа к веб-серверу
EXPOSE 80

# Запускаем Nginx
CMD ["nginx", "-g", "daemon off;"]
