FROM python:3.9-slim

WORKDIR /app

RUN apt-get update && apt-get install -y gcc libpq-dev
RUN pip install fastapi uvicorn psycopg2-binary sqlalchemy

COPY main.py .

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
