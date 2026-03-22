FROM python:3.11-slim

WORKDIR /app
# First, copy only the list of dependencies (to cache Docker layers)
COPY requirements.txt .
# Requests, psycopg2-binary and prometheus_client
RUN pip install --no-cache-dir -r requirements.txt

COPY monitor.py .

CMD ["python", "monitor.py"]
