import requests
import time
import os
import psycopg2
from prometheus_client import start_http_server, Counter, Gauge
import time

# Create metrics
REQUEST_COUNT = Counter('site_requests_total', 'Total status checks', ['site', 'status'])
RESPONSE_TIME = Gauge('site_response_time_seconds', 'Response time in seconds', ['site'])

SITES = os.getenv('SITES_TO_CHECK', "https://google.com,https://github.com").split(",")
# Connection settings
DB_CONFIG = "host=db dbname=monitoring user=admin password=qwerty123"

STATUS_MESSAGES = {
    200: "The site is working great!",
    404: "Page not found (check the URL).",
    500: "Server error: it's down.",
    502: "Bad gateway (server is overloaded).",
    503: "Service temporarily unavailable."
}

def log_to_file(text): # Writing file to a compute
    if not os.path.exists("reports"): os.makedirs("reports")
    with open("reports/monitoring_log.txt","a") as f:
        f.write(f"{time.ctime()} | {text}\n")
    
def log_to_db(site, code, msg):
    try:
        with psycopg2.connect(DB_CONFIG) as conn:
            conn.autocommit = True # Autocommit
            with conn.cursor() as cur:
                cur.execute("INSERT INTO site_logs (site_url, status_code, message) VALUES (%s, %s, %s)", (site, code, msg))
    except Exception as e:
        print(f"The DataBase is currently unavailable: {e}")

def init_db(): # Create the table
    try:
        with psycopg2.connect(DB_CONFIG) as conn:
            with conn.cursor() as cur:
                cur.execute("""
                    CREATE TABLE IF NOT EXISTS site_logs (
                        id SERIAL PRIMARY KEY,
                        check_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                        site_url TEXT,
                        status_code INTEGER,
                        message TEXT
                    );
                """)
                print("Table 'site_logs' is ready.")
    except Exception as e:
        print(f"DB table check failed: {e}")

if __name__ == "__main__": # Monitoring will continue while the script is running
    print("Waiting for DB to start...")
    time.sleep(10) # Waiting for the DB to start
    
    init_db() # Сreating the table before the loop
    
    # Start the metrics server on port 8000
    # Prometheus will access this at: http://checker:8000/metrics
    start_http_server(8000)
    print("Prometheus metrics server started on port 8000")

    while True:
        for site in SITES:
            site = site.strip()
            start_time = time.time() # We record the start time of the request
            
            try:
                r = requests.get(site, timeout=5)
                status_code = r.status_code
                msg = STATUS_MESSAGES.get(status_code, f"Code {status_code}")
            except Exception:
                status_code = 0
                msg = "Offline"

            # We update the metrics after every transaction
            REQUEST_COUNT.labels(site=site, status=status_code).inc()
            RESPONSE_TIME.labels(site=site).set(time.time() - start_time)

            log_to_file(f"{site} -> {msg}")
            log_to_db(site, status_code, msg)
            print(f"Checked {site}: {msg}")

        time.sleep(60)