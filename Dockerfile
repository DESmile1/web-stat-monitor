FROM python:3.11-slim

WORKDIR /app
# PosgreSQL lib
RUN pip install requests psycopg2-binary

COPY monitor.py .

CMD ["python", "monitor.py"]