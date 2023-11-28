FROM ubuntu:22.04

RUN apt update && apt -y install python3 pip

WORKDIR /code

COPY requirements.txt .
RUN python3 -m pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./src /code/src
COPY ./tests /code/tests
COPY ./db_test_data.json /code/db_test_data.json
COPY ./.env /code/.env
COPY ./start.sh /code/start.sh


RUN ["chmod", "+x", "start.sh"]

EXPOSE 8000:8000

CMD ["./start.sh"]