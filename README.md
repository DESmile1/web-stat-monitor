# Web Status Monitor (Docker Edition)
![Python Code Check](https://github.com/DESmile1/web-stat-monitor/actions/workflows/check_code.yml/badge.svg)
A simple and reliable tool for monitoring website availability, packaged in Docker.
The project has evolved from a script into a microservice-based system with a database.

## Tech Stack
- **Python 3.11**: Core logic (`requests` library).
- **PostgreSQL 15**: Relational database for storing log history.
- **Prometheus**: Time-series database for collecting metrics.
- **Grafana**: Professional dashboards for real-time visualization.
- **Adminer**: Web interface for managing the PostgreSQL database in a browser.
- **Docker & Docker Compose**: Containerization and orchestration of all services.
- **GitHub Actions**: Automated code quality checking (Linter/PEP8).

## Architecture
The project is deployed in an isolated Docker network and consists of three services:
1. **checker**: A Python script that polls websites and performs double logging.
2. **db**: The official PostgreSQL image. Stores the `site_logs` table.
3. **prometheus**: Scraper that collects data from the checker every 15s.
4. **grafana**: Visualization tool accessible via port 3000.
5. **adminer**: Accessible via port `8080` for visual data monitoring.

## CI/CD (Automation)
A **GitHub Actions** pipeline is configured in the project:
- **Linting**: Every time there is a `git push` to the `main` branch, a `flake8` check runs. It looks for syntax errors and ensures code cleanliness (PEP 8).
- The check status is displayed as a badge at the top of this file.

## Features
- **Dual Logging**: Data is written simultaneously to the text file `./logs/monitoring_log.txt` and to a database table.
- **Auto-DB-Init**: The script automatically creates the table schema in PostgreSQL on first run (`IF NOT EXISTS`).
- **Real-time Metrics**: Monitor latency and status codes on live charts.
- **Infrastructure as Code**: All monitoring is launched with a single command.
- **Smart Messages**: Custom messages for HTTP status codes (200, 404, 500, etc.) via a Python dictionary.
- **Security**: All passwords are stored in environment variables (`.env`).
- **Data Persistence**: Uses Docker Volumes to preserve database data even after containers are deleted.

## Access Points
| Service | URL | What's in there? |
| :--- | :--- | :--- |
| **Grafana** | [http://localhost:3000](http://localhost:3000) | Main dashboard with charts (Логин: `admin`) |
| **Prometheus** | [http://localhost:9090](http://localhost:9090) | Metrics database (for query debugging) |
| **Adminer** | [http://localhost:8080](http://localhost:8080) | PostgreSQL Administration (Viewing Logs in a Table) |
| **Metrics** | [http://localhost:8000/metrics](http://localhost:8000/metrics) | Raw data from a Python script (for Prometheus) |

## How to Run

1. Make sure you have **Docker** and **Docker Compose** installed.
2. Clone the repository.
3. Create a .env file (use .env.example as a template) and set your passwords.
4. Run the project with a single command:
   ```bash
   docker-compose up --build -d