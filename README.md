# Web Status Monitor (Docker Edition)

A simple and reliable tool for monitoring website availability, packaged in Docker.

## Features
- **Python script**: Uses the `requests` library to check status codes.
- **Dockerized**: Fully isolated environment; no Python installation required on the host.
- **Docker Compose**: Manage the list of sites via environment variables.
- **Error Handling**: Handles exceptions (timeouts, no connection) and displays clear error messages.

## How to Run

1. Make sure you have **Docker** and **Docker Compose** installed.
2. Clone the repository.
3. Run the project with a single command:
   ```bash
   docker-compose up -d
