FROM python:3.12

LABEL maintainer="Sparsh Bamrara"

RUN pip3 install --upgrade pip

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

ENV PYTHONWARNINGS=ignore
ENV DEBUG=no
ENV API_KEY = my-api-key
ENV DB_USERNAME = postgres
ENV DB_PASSWORD = 1234
ENV DB_HOST = localhost
ENV DB_PORT = 5432
ENV DATABASE = game_db

ENTRYPOINT ["python3"]

CMD ["main.py"]
