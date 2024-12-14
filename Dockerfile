FROM python:3.12

LABEL maintainer="Sparsh Bamrara"

RUN pip3 install --upgrade pip

WORKDIR /app

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . .

ENV PYTHONWARNINGS=ignore
ENV DEBUG=no

ENTRYPOINT ["python3"]

CMD ["main.py"]
