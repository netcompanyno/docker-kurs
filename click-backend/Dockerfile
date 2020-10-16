FROM python:3.7-alpine

WORKDIR /code

COPY requirements.txt .
RUN pip install -r requirements.txt

EXPOSE 5000

COPY app.py .

ENV FLASK_RUN_HOST=0.0.0.0

CMD ["flask", "run"]
