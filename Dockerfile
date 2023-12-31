# Этап 1: Соберите HTML документацию
FROM sphinxdoc/sphinx:6.2.1

# Переменная окружения PYTHONUNBUFFERED, чтобы вывод был немедленно показан в консоли
ENV PYTHONUNBUFFERED=1

# Установка системных зависимостей
RUN apt-get update
RUN apt-get install make graphviz plantuml --yes --no-install-recommends

WORKDIR /docs
COPY . /docs

# Установите зависимости из файла requirements.txt и перенаправьте вывод в stdout (параметр 2>&1)
RUN pip install --no-cache-dir -r requirements.txt -v 2>&1

# Соберите HTML документацию и перенаправьте вывод в stdout (параметр 2>&1)
RUN make html 2>&1

RUN ls /docs/build/html
