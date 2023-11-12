FROM ubuntu:22.04

RUN apt update && apt -y install python3 pip

WORKDIR /code

COPY ./start.sh /code/start.sh

COPY ./requirements.txt /code/requirements.txt
RUN python3 -m pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY ./src /code/src

RUN ["chmod", "+x", "start.sh"]

EXPOSE 8000:8000

CMD ["./start.sh"]