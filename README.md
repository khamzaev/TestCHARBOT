# Telegram-бот с интеграцией Google Sheets

Этот проект представляет собой Telegram-бота, который взаимодействует с пользователями через команды и инлайн-кнопки, получает данные из API, сохраняет их в базу данных и добавляет в Google Sheets. Проект реализован с использованием современных Python-библиотек, таких как `aiogram`, `aiohttp` и `googleapiclient`.

---

## Возможности

- **Интеграция с Telegram**:
  - Обработка команды `/start` с приветственным сообщением и инлайн-кнопками.
  - Получение данных из внешнего API (например, JSONPlaceholder) по запросу пользователя.

- **Обработка данных**:
  - Преобразование данных из формата `camelCase` в `snake_case`.
  - Валидация и обработка данных с использованием моделей Pydantic.

- **Работа с базой данных**:
  - Сохранение обработанных данных в базе данных PostgreSQL.

- **Интеграция с Google Sheets**:
  - Добавление обработанных данных в указанный лист Google Sheets.

- **Поддержка вебхуков**:
  - Использование `aiohttp` для обработки обновлений Telegram через вебхуки.

---

## Требования

Для запуска проекта вам потребуется:

1. Python 3.10+
2. Токен Telegram-бота, полученный через [BotFather](https://core.telegram.org/bots#botfather).
3. Учетные данные сервисного аккаунта Google Cloud с доступом к Google Sheets API.
4. Docker (опционально, для контейнеризации).

---

## Установка и настройка

### 1. Клонирование репозитория
```bash
git clone https://github.com/khamzaev/TestCHARBOT.git
cd TestCHARBOT
```

### 2. Создание виртуального окружения и установка зависимостей
```bash
python -m venv venv
source venv/bin/activate  # На Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Настройка переменных окружения
Создайте файл `.env` в корневой директории проекта и добавьте:
```
TELEGRAM_API_TOKEN=ваш-токен-бота
GOOGLE_CREDENTIALS_FILE=путь-к-файлу-учетных-данных.json
GOOGLE_SPREADSHEET_ID=идентификатор-google-таблицы
WEBHOOK_URL=https://ваш-домен.com/webhook
POSTGRES_URL=postgresql+asyncpg://username:password@localhost/db_name
```

### 4. Инициализация базы данных
Выполните следующую команду для инициализации базы данных:
```bash
python -m app.db
```

---

## Запуск бота

### 1. Запуск сервера вебхуков
Запустите бота с помощью:
```bash
python app/bot.py
```

### 2. Тестирование бота
- Отправьте команду `/start` в чат с ботом в Telegram, чтобы начать взаимодействие.
- Нажмите кнопку **Fetch Data**, чтобы получить данные из API и обработать их.

---

## Структура проекта

```plaintext
.
├── app/
│   ├── handlers/
│   │   ├── __init__.py                # Инициализация пакета
│   │   ├── start.py                   # Хендлеры Telegram-бота
│   ├── models/
│   │   ├── __init__.py                # Инициализация пакета
│   │   ├── data_model.py              # Модели данных (Pydantic)
│   ├── services/
│   │   ├── __init__.py                # Инициализация пакета
│   │   ├── data_service.py            # Логика обработки и сохранения данных
│   │   ├── api_client.py              # Клиент для работы с внешним API
│   │   ├── google_sheets_client.py    # Интеграция с Google Sheets
│   ├── bot.py                         # Telegram-бот
│   ├── db.py                          # Работа с базой данных
│   ├── di_container.py                # Настройка Dependency Injection
│   ├── utils.py                       # Утилиты
├── nginx/
│   ├── nginx.conf                     # Конфигурация Nginx
├── config.py                          # Конфигурация проекта
├── credentials.json                   # Учетные данные Google Cloud
├── docker-compose.yml                 # Docker Compose файл
├── Dockerfile                         # Dockerfile для контейнеризации
├── README.md                          # Документация проекта
├── requirements.txt                   # Зависимости Python
```

---

## Основные компоненты

### 1. Хендлеры Telegram (`start.py`)
- Обрабатывают команду `/start` и нажатия инлайн-кнопок.
- После нажатия кнопки **Fetch Data**:
  - Получают данные из внешнего API (например, `posts`).
  - Сохраняют данные в базу данных.
  - Добавляют данные в Google Sheets.

### 2. Сервис работы с данными (`data_service.py`)
Реализует основную бизнес-логику:
- Получает и обрабатывает данные из API.
- Сохраняет данные в базу данных.
- Добавляет данные в Google Sheets.

### 3. Интеграция с Google Sheets (`google_sheets_client.py`)
Обрабатывает добавление строк в указанную таблицу Google Sheets через API Google Sheets.

### 4. Клиент API (`api_client.py`)
Получает данные из внешнего API и преобразует ключи из `camelCase` в `snake_case`.

### 5. Утилиты (`utils.py`)
Содержит вспомогательные функции, такие как `camel_to_snake` и `transform_keys` для изменения формата ключей.

---

## Автор

- GitHub: [khamzaev](https://github.com/khamzaev)