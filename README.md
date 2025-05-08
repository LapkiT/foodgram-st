# Foodgram - Социальная сеть для любителей готовить

## О проекте

"Продуктовый помощник" - это сервис, где пользователи могут публиковать свои рецепты, подписываться на публикации других и формировать список продуктов для покупки. Я разработал полноценное веб-приложение, включающее современный бэкенд на Django REST Framework и интерактивный фронтенд на React.

## Стек технологий

- **Backend**:

  - Python 3.11
  - Django 4.x
  - Django REST Framework
  - PostgreSQL 13.3
  - Docker

- **Frontend**:

  - React
  - Node.js 21

- **Инфраструктура**:
  - Nginx 1.25
  - Docker Compose
  - GitHub Actions (опционально)

## Установка и запуск

### Требования

- Docker и Docker Compose
- Git

### Процесс развертывания

1. **Получение кода**:

   ```bash
   git clone <ваш-репозиторий>
   cd foodgram-st
   ```

2. **Создание файла переменных окружения**:

   Создайте файл `.env` в директории `backend/foodgram_backend/`:

   ```
   POSTGRES_DB=foodgram_db
   POSTGRES_USER=foodgram_user
   POSTGRES_PASSWORD=secure_password
   POSTGRES_HOST=db
   POSTGRES_PORT=5432
   SECRET_KEY=your-django-secret-key
   DEBUG=False
   ALLOWED_HOSTS=127.0.0.1,localhost,backend
   ```

3. **Запуск проекта**:

   ```bash
   # Перейдите в директорию с docker-compose
   cd infra

   # Запустите сборку и старт контейнеров
   docker-compose up -d --build

   # Выполните миграции
   docker-compose exec backend python manage.py migrate

   # Загрузите тестовые данные
   docker-compose exec backend python manage.py loaddata ../data/foodgram_data.json

   # Создайте администратора
   docker-compose exec backend python manage.py createsuperuser
   ```

## Функциональность

- Регистрация и авторизация пользователей
- Создание, просмотр, редактирование и удаление рецептов
- Фильтрация рецептов по тегам
- Добавление рецептов в избранное
- Подписки на авторов
- Добавление рецептов в список покупок и скачивание этого списка

## Доступ к проекту

После запуска проект будет доступен:

- **Главная страница**: http://localhost/
- **Панель администратора**: http://localhost/admin/
- **Документация API**: http://localhost/api/docs/

## Дополнительно

Для управления проектом доступны следующие команды:

```bash
# Остановка проекта
docker-compose down

# Просмотр логов
docker-compose logs -f

# Пересборка контейнеров
docker-compose up -d --build
```

## Создание тестовых аккаунтов

После запуска приложения вы можете создать тестовые аккаунты через админ-панель Django (`http://localhost/admin/`) или через API. Для создания пользователя через API используйте эндпоинт `/api/users/`.

## Дополнительные команды

### Загрузка ингредиентов

Для загрузки ингредиентов из файла (например, `ingredients.json` или `ingredients.csv`) в папке `data/`:

## Настройка CI/CD (Continuous Integration и Continuous Deployment)

Проект настроен для использования GitHub Actions для автоматического тестирования, сборки и публикации Docker-образов в Docker Hub, а также для автоматического деплоя на удаленный сервер.

### Что происходит в процессе CI/CD:

1. **Тестирование**:

   - Проверка кода с использованием Flake8

2. **Сборка и публикация образов**:

   - Сборка Docker-образа для бэкенда и публикация на Docker Hub
   - Сборка Docker-образа для фронтенда и публикация на Docker Hub

3. **Деплой**:
   - Автоматическая доставка и запуск приложения на боевом сервере

### Необходимые настройки:

Для работы CI/CD необходимо установить следующие секреты в настройках GitHub-репозитория:

- `DOCKER_USERNAME` - имя пользователя в Docker Hub
- `DOCKER_PASSWORD` - пароль от Docker Hub
- `HOST` - IP-адрес удаленного сервера
- `USER` - имя пользователя на сервере
- `SSH_KEY` - приватный SSH-ключ
- `PASSPHRASE` - парольная фраза для SSH-ключа (если есть)
- `SECRET_KEY` - секретный ключ Django
- `POSTGRES_DB` - имя базы данных
- `POSTGRES_USER` - имя пользователя для базы данных
- `POSTGRES_PASSWORD` - пароль пользователя базы данных

Подробную информацию о настройке CI/CD можно найти в [инструкции по настройке](./.github/README.md).
