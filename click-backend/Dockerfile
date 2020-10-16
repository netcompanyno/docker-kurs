FROM python:3.7-alpine

WORKDIR /code

RUN pip install -r requirements.txt

EXPOSE 5000

COPY app.py .

# Sett miljøvariabel her

CMD ["flask", "run"]
