# Web Status Monitor (Docker Edition)

A simple and reliable tool for monitoring website availability, packaged in Docker.
The project has evolved from a script into a microservice-based system with a database.
## Features

- **Python script**: Uses the `requests` library to check status codes.
- **Dockerized**: Fully isolated environment; no Python installation required on the host.
- **Docker Compose**: Manage the list of sites via environment variables.
- **Error Handling**: Handles exceptions (timeouts, no connection) and displays clear error messages.
- **PostgreSQL 15**: A reliable storage solution for monitoring logs.
**Adminer**: A lightweight web interface for managing databases (accessible via a browser).

## Architecture

1. **checker**: That Python script. It checks websites and sends reports to two destinations at once.
2. **db**: A PostgreSQL database that stores the history of all checks.
3. **adminer**: A tool for visually viewing database tables.

## How to Run

1. Make sure you have **Docker** and **Docker Compose** installed.
2. Clone the repository.
3. Run the project with a single command:
   ```bash
   docker-compose up -d
