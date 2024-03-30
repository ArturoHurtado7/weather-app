# Build Python
FROM python:3.11.3 AS py-builder
WORKDIR /app
COPY ./backend/requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY ./backend ./
COPY .env ./

CMD ["python", "main.py"]