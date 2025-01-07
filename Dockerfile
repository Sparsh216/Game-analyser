FROM python:3.12

LABEL maintainer="Sparsh Bamrara"

RUN pip3 install --upgrade pip

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

ENV PYTHONWARNINGS=ignore \
    DEBUG=no \
    API_KEY=my-api-key \
    DB_USERNAME=postgres \
    DB_PASSWORD=1234 \
    DB_HOST=localhost \
    DB_PORT=5432 \
    DATABASE=game_db

ENTRYPOINT ["python3"]

CMD ["main.py"]
