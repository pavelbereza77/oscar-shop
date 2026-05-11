FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /code

# Установка системных зависимостей
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    libpq-dev \
    libssl-dev \
    libffi-dev \
    && rm -rf /var/lib/apt/lists/*

# Файл: src/Dockerfile

# ... другие строки (FROM, WORKDIR и т.д.) ...

# --- ЭТО НУЖНО ИСПРАВИТЬ/ДОБАВИТЬ ---
# Копируем файл со списком зависимостей в образ
COPY requirements.txt .

# ОДНА команда RUN, которая делает ВСЁ:
# 1. Обновляет pip
# 2. Устанавливает зависимости из requirements.txt
# 3. Удаляет конфликтный файл миграций
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt 
    # && 
    #\
    # rm -f /usr/local/lib/python3.11/site-packages/oscar/apps/customer/migrations/0008_assign_permissions_to_staff.py

# ... остальные строки (COPY . . и т.д.) ...
# Копируем entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Копируем весь проект
COPY . .

# Настройки для Gunicorn
EXPOSE 8000

# Entrypoint и Command (если не используется docker-compose.yml)
# ENTRYPOINT ["/entrypoint.sh"]
# CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]



# FROM python:3.11

# ENV PYTHONDONTWRITEBYTECODE=1 \
#     PYTHONUNBUFFERED=1

# WORKDIR /code

# # Сначала системные зависимости
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     gcc \
#     libpq-dev \
#     && rm -rf /var/lib/apt/lists/*

# # Копируем и устанавливаем зависимости Python
# COPY requirements.txt .
# RUN pip install --upgrade pip && \
#     pip install --no-cache-dir -r requirements.txt

# # Копируем entrypoint
# COPY entrypoint.sh /entrypoint.sh
# RUN chmod +x /entrypoint.sh

# # Копируем весь проект
# COPY . .

# EXPOSE 8000

# ENTRYPOINT ["/entrypoint.sh"]
# CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]


# # Базовый образ
# FROM python:3.11-slim

# # Переменные окружения для Python
# ENV PYTHONDONTWRITEBYTECODE=1 \
#     PYTHONUNBUFFERED=1

# # Устанавливаем рабочую директорию
# WORKDIR /code

# # --- НАЧАЛО ИЗМЕНЕНИЙ ---
# # Копируем скрипт точки входа и делаем его исполняемым
# COPY entrypoint.sh /entrypoint.sh
# RUN chmod +x /entrypoint.sh
# ENTRYPOINT ["/entrypoint.sh"]
# # --- КОНЕЦ ИЗМЕНЕНИЙ ---

# # Копируем зависимости и устанавливаем их
# COPY requirements.txt .
# RUN pip install --upgrade pip && \
#     pip install --no-cache-dir -r requirements.txt

# # Копируем весь код проекта (ЭТО ГЛАВНАЯ КОМАНДА)
# COPY . .

# # Установка системных зависимостей (для сборки)
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     gcc \
#     libpq-dev \
#     && rm -rf /var/lib/apt/lists/*

# EXPOSE 8000

# --- НАЧАЛО ИЗМЕНЕНИЙ ---
# Исправленная команда для Gunicorn (убрано лишнее 'config.')
# CMD ["gunicorn", "config.wsgi:application", "--bind", "0.0.0.0:8000"]
# --- КОНЕЦ ИЗМЕНЕНИЙ ---


# # Базовый образ
# FROM python:3.11-slim

# # Переменные окружения для Python
# ENV PYTHONDONTWRITEBYTECODE=1 \
#     PYTHONUNBUFFERED=1

# # Устанавливаем рабочую директорию
# WORKDIR /code

# # Копируем зависимости и устанавливаем их
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# # Копируем весь код проекта (ЭТО ГЛАВНАЯ КОМАНДА)
# COPY . .

# # Установка системных зависимостей (для сборки)
# RUN apt-get update && apt-get install -y --no-install-recommends \
#     gcc \
#     libpq-dev \
#     && rm -rf /var/lib/apt/lists/*

# EXPOSE 8000

# # Команда по умолчанию при запуске контейнера
# CMD ["gunicorn", "config.config.wsgi:application", "--bind", "0.0.0.0:8000"]
