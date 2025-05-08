# Настройка CI/CD для проекта Foodgram

Этот документ содержит инструкции по настройке непрерывной интеграции и развертывания (CI/CD) для проекта Foodgram с использованием GitHub Actions и Docker Hub.

## Необходимые секреты GitHub

Для правильной работы CI/CD pipeline необходимо добавить следующие секреты в настройки репозитория GitHub:

1. `DOCKER_USERNAME` - ваше имя пользователя на Docker Hub
2. `DOCKER_PASSWORD` - ваш пароль или токен доступа к Docker Hub
3. `HOST` - IP-адрес сервера для деплоя
4. `USER` - имя пользователя на сервере
5. `SSH_KEY` - приватный SSH-ключ для доступа к серверу
6. `PASSPHRASE` - фраза-пароль для SSH-ключа (если есть)
7. `SECRET_KEY` - секретный ключ для Django
8. `POSTGRES_DB` - имя базы данных PostgreSQL
9. `POSTGRES_USER` - имя пользователя PostgreSQL
10. `POSTGRES_PASSWORD` - пароль пользователя PostgreSQL

## Как добавить секреты в GitHub

1. Перейдите в свой репозиторий на GitHub
2. Нажмите на вкладку "Settings"
3. В левой панели выберите "Secrets and variables" -> "Actions"
4. Нажмите "New repository secret"
5. Введите имя и значение секрета, затем нажмите "Add secret"
6. Повторите шаги 4-5 для всех необходимых секретов

## Как работает процесс CI/CD

Workflow для CI/CD настроен следующим образом:

1. **Тесты**: Запускаются проверки кода с использованием flake8.
2. **Сборка и публикация образов Docker**:
   - Собирается Docker-образ для бэкенда и публикуется на Docker Hub.
   - Собирается Docker-образ для фронтенда и публикуется на Docker Hub.
3. **Деплой на сервер**:
   - Копирование необходимых файлов на сервер.
   - Создание или обновление файла `.env` с переменными окружения.
   - Обновление docker-compose.yml для использования образов с Docker Hub.
   - Запуск контейнеров с использованием docker-compose.
   - Выполнение миграций и сбор статических файлов.

## Настройка Docker Hub

1. Создайте аккаунт на [Docker Hub](https://hub.docker.com/) если у вас его еще нет.
2. Создайте два репозитория:
   - `foodgram_backend` - для бэкенд-части проекта
   - `foodgram_frontend` - для фронтенд-части проекта

## Подготовка сервера

На вашем сервере должен быть установлен Docker и Docker Compose. Для установки:

```bash
# Обновление пакетов
sudo apt update
sudo apt upgrade -y

# Установка необходимых пакетов
sudo apt install apt-transport-https ca-certificates curl software-properties-common -y

# Добавление Docker GPG ключа
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -

# Добавление репозитория Docker
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

# Установка Docker
sudo apt update
sudo apt install docker-ce -y

# Установка Docker Compose
sudo curl -L "https://github.com/docker/compose/releases/download/v2.21.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod +x /usr/local/bin/docker-compose

# Добавление текущего пользователя в группу docker
sudo usermod -aG docker $USER
```

После настройки сервера и добавления всех секретов в GitHub, workflow будет автоматически запускаться при каждом push в основную ветку (main или master).
