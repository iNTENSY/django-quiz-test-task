Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке:
```
git clone https://github.com/iNTENSY/quiz.git
```
```
cd quiz
```
___
Вам потребуется создать файл .env

Реализуйте его по примеру из .env.example
___
Для локального тестирования вручную (не через Docker)

Создать и активировать виртуальное окружение:

```shell
python3 -m venv env
.\venv\Scripts\activate
```

Установить зависимости из файла requirements.txt:
```shell
python3 -m pip install --upgrade pip
pip install -r requirements.txt
```

Выполнить миграции:
```shell
python3 manage.py migrate
```
Запустить проект:

```shell
python3 manage.py runserver
```
___
Для тестирования через Docker

Собрать и запустить контейнер
```docker
docker-compose build
docker-compose up
```
