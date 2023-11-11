# fastapi-get-form
Web-приложение для определения заполненных форм

## Usage
### Скачиваем проект
### Поднимаем контейнер с mongodb
```
docker run -d -p 27017:27017 --name mongo_container mongo
```
Если образ mongodb не установлен локально, то он установится автоматически
### Настраиваем приложение
Находясь в директории проекта:
Создаем виртуальное окружение
```
python3 -m venv venv
```
Активируем виртуальное окружение (Linux)
```
source venv/bin/activate
```
Устанавливаем зависимости
```
python3 -m pip install -r requirements.txt
```
### Заполняем базу mongodb тестовыми данными
```
python3 src/database.py
```
В консоли видим тестовые данные
### Выполняем тестовые запросы
```
python3 -m pytest
```
Видим результаты тестов
### Запускаем веб-приложение
Выполняем команду
```
uvicorn src.main:app --reload
```
Переходим на [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) и выполняем нужные запросы.
### Эндпоинты
1. get "/" — index, возвращает строку "Hello world!"
2. post "/get_form" — основной эндпоинт определения заполненной формы, возвращает имя максимально подходящей формы, если такой нет, возвращает список типизированных полей
3. get "/db" — получение всех документов коллекции с тестовыми данными mongodb