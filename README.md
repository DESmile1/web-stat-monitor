# Web Status Monitor (Docker Edition)
![Python Code Check](https://github.com/DESmile1/web-stat-monitor/actions/workflows/check_code.yml/badge.svg)
A simple and reliable tool for monitoring website availability, packaged in Docker.
The project has evolved from a script into a microservice-based system with a database.

## Tech Stack
- **Python 3.11**: Core logic (`requests` library).
- **PostgreSQL 15**: Relational database for storing log history.
- **Adminer**: Web interface for managing the database in a browser.
- **Docker & Docker Compose**: Containerization and orchestration of all services.
- **GitHub Actions**: Automated code quality checking (Linter).

## Architecture
The project is deployed in an isolated Docker network and consists of three services:
1. **checker**: A Python script that polls websites and performs double logging.
2. **db**: The official PostgreSQL image. Stores the `site_logs` table.
3. **adminer**: Accessible via port `8080` for visual data monitoring.

## CI/CD (Automation)
A **GitHub Actions** pipeline is configured in the project:
- **Linting**: Every time there is a `git push` to the `main` branch, a `flake8` check runs. It looks for syntax errors and ensures code cleanliness (PEP 8).
- The check status is displayed as a badge at the top of this file.

## Features
- **Dual Logging**: Data is written simultaneously to the text file `./logs/monitoring_log.txt` and to a database table.
- **Auto-DB-Init**: The script automatically creates the table schema in PostgreSQL on first run (`IF NOT EXISTS`).
- **Smart Messages**: Custom messages for HTTP status codes (200, 404, 500, etc.) via a Python dictionary.
- **Data Persistence**: Uses Docker Volumes to preserve database data even after containers are deleted.

## How to Run

1. Make sure you have **Docker** and **Docker Compose** installed.
2. Clone the repository.
3. Run the project with a single command:
   ```bash
   docker-compose up --build -d