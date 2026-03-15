FROM python:3.11-slim

WORKDIR /app

RUN pip install requests

COPY monitor.py .

CMD ["python", "monitor.py"]