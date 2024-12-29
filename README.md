# Diploma_Work

# Доска объявлений. Backend

## Команды для управления сервером:

### 1. Запуск сервера:
```
python manage.py runserver
```


### Безопасность
Для проекта настроен CORS, чтобы фронтенд мог подключаться к проекту на развернутом сервере./n
Сайт - https://pypi.org/project/django-cors-headers/

## Flake8
— это инструмент для проверки стиля и качества кода на Python. Он позволяет просканировать код проекта и обнаружить в нём стилистические ошибки и нарушения различных конвенций кода
### Установка flake8:
```
python -m pip install flake8
```
### Чтобы запустить Flake8 на Python, нужно ввести в командной строке:
```
flake8 config
```

### Если вы пользуетесь pip (менеджер установки пакетов), то все зависимости можно установить с файла [requirements.txt](requirements.txt), выполнив команду в командной строке: 
```
pip install -r requirements.txt
```

### Для сохранения фикстур используем команду:
```
python -Xutf8 manage.py dumpdata name_app(имя приложения) --indent 2 -o name_app.json
```

### Для работы с тестами используется библиотека 
- **coverage==7.6.8**

### Для выполнения тестов используем команду:
```
coverage run -m pytest
```

### Для статистики покрытия тестами проекта используем команду:
```
coverage report
```

# Работа с Docker
### В командной строке проверяем версию командой:  
```
docker version
```
### Тестируем докер командой:  
```
docker run hello-world
```
### Для взаимодействия сервиса postgresql и приложения создаем единую сеть командой:  
```
docker network create DW
```
### Создаем контейнер postgres командой: 
```
docker run -d --network=DW --name=postgres_container -p 5432:5432 -e POSTGRES_DB=DW -e POSTGRES_USER=user -e POSTGRES_PASSWORD=201023 postgres:latest
```
### Операции с контейнером см. раздел “Команды в Docker”, вот некоторые из них:
-```docker compose up --build``` - построит Docker-образы и запустит контейнеры для приложения и базы данных
- ```docker stop postgres_container``` - останавливает запущенный контейнер
- ```docker rm postgres_container``` - удаляет контейнер
- ```docker ps -a``` - показывает и запущенные и остановленные контейнеры (флаг "-а")
- ```docker exec -it 53e bash``` - запустит интерактивную оболочку Bash в контейнере с ID 53e (первые 3 символа ID контейнера)
### Загрузка официального образа Python командой: 
```
docker pull python
```
- Команда скачивает в систему последнюю версию образа Python (сайт -  python - Official Image | Docker Hub)
### Соберите образ с помощью команды:
```
docker-compose build
```
### Запустите контейнеры с помощью команды:
```
docker-compose up
```
**Последние 2 команды можно объединить в одну команду:**
```
docker-compose up -d --build
```
### Для остановки и удаления контейнеров используйте Ctrl + C в терминале, где запущен **docker-compose up**
### Для остановки контейнеров и удаления созданных ресурсов выполните команду:

```
docker-compose down
```

### После запуска доступность сервисов можно проверить командой:
```
docker-compose ps
```

## Файл docker-compose.yaml состоит из нескольких разделов:
- **version**. Директива определяет версию синтаксиса Docker Compose, используемого в файле. 
- **services**. Раздел определяет контейнеры, которые Compose должен создать и запустить. Каждый сервис представляет собой отдельный контейнер с определённой конфигурацией. 
- **volumes**. Раздел используется для определения томов, которые могут быть подключены к контейнерам для хранения данных. 
- **networks**. Раздел позволяет определить пользовательские сети, в которых будут работать контейнеры, что обеспечивает изоляцию и настройку сетевых подключений. 
- **environment**. Директива задаёт переменные окружения для контейнера. 
- **depends_on**. Директива указывает, что данный сервис зависит от других сервисов и должен быть запущен после них. 

### Запуск отложенных и периодических задач:
1. Запуск обработчика очереди (worker) для получения задач и выполнения их выполняется командой:
```
celery -A config worker -l INFO
```
Где:
- **config** — директория с конфигурацией Django-проекта;
- **worker** — тип запуска, данный параметр запускает обработчик задач из очереди;
- **-l INFO** — уровень логирования.
**!!!** *Обратите внимание, что для Windows при указании обработчика событий необходимо добавить флаг -P eventlet, для этого установите модуль eventlet==0.38.0* **!!!**
2. Запуск Celery worker и планировщика Celery beat.
- *Чтобы использовать периодические задачи, нужно запустить не только Celery worker, но и планировщик Celery beat. Выполните следующую команду в командной строке:*
```
celery -A config worker —loglevel=info
```
```
celery -A config beat —loglevel=info
```
Это запустит Celery worker и планировщик Celery beat, которые будут совместно работать для выполнения периодических задач.

### 3. Настройка и примеры работы с Celery: https://docs.celeryq.dev.
### 4. Работа и настройка celery-beat: https://django-celery-beat.readthedocs.io/. 
### 5. Официальный сайт Redis, на котором можно найти инструкции по установке, а также документацию по работе с консольным интерфейсом: https://redis.io/. 


# Данное приложение решает следующие задачи:
- Авторизация и аутентификация пользователей.
- Распределение ролей между пользователями (пользователь и админ).
- Восстановление пароля через электронную почту.
- CRUD для объявлений на сайте.
- Под каждым объявлением пользователи могут оставлять отзывы.
- В заголовке сайта можно осуществлять поиск объявлений по названию.
- Отслеживание активности пользователей с помощью пакета celery, с отправкой данных в телеграмм(в разработке).