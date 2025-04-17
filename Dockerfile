# Используем минимизированный образ Python
FROM python:3.11-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Обновляем систему и устанавливаем зависимости для Python
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Копируем только файл зависимостей для использования кеша Docker
COPY requirements.txt .

# Устанавливаем Python-зависимости в виртуальное окружение
RUN python -m venv /opt/venv && \
    /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

# Обеспечиваем доступ к виртуальному окружению
ENV PATH="/opt/venv/bin:$PATH"

# Копируем остальную часть проекта
COPY . .

# Создаем непривилегированного пользователя и переключаемся на него
RUN useradd -m nonroot
USER nonroot

# Указываем команду запуска
CMD ["python", "app/bot.py"]
