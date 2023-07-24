# Этап 1: Соберите HTML документацию
FROM python:3.9 as builder

WORKDIR /app
COPY . /app

# Установите зависимости
RUN pip install sphinx-book-theme

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
