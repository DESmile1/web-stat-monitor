import requests
import time
import os
import psycopg2

SITES = os.getenv('SITES_TO_CHECK', "https://google.com,https://github.com").split(",")
# Connection settings
DB_CONFIG =  "host=db dbname=monitoring user=admin password=qwerty123"

STATUS_MESSAGES = {
    200: "The site is working great!",
    404: "Page not found (check the URL).",
    500: "Server error: it's down.",
    502: "Bad gateway (server is overloaded).",
    503: "Service temporarily unavailable."
}

def log_to_file(text): # Writing file to a computer
    if not os.path.exists("reports"): os.makedir("reports")
    with open("reports/monitoring_log.txt","a") as f:
        f.write(f"{time.ctime()} | {text}\n")
    
def log_to_db(site, code, msg):
        try:
             with psycopg2.connect(DB_CONFIG) as conn:
                  with conn.cursor() as cur:
                       cur.execute("INSERT INTO site_url (site_url, status_code, message) VALUES (%s, %s, %s)", (site, code, msg))

        except:
             print("The DataBase is currentsy unavailable")

if __name__ == "__main__": # Monitoring will continue while the script is running
   time.sleep(10) # Waiting for the DB to start
   while True:
        for site in SITES:
            site = site.strip()
            try:
                 r = requests.get(site, timeout=5)
                 msg = STATUS_MESSAGES.get(r.status_code, f"Code {r.status_code}")
            except:
                 r, msg = type('obj', (object,), {'status_code':0}), "Offline"

            log_to_file(f"{site} -> {msg}")
            log_to_db(site, r.status_code, msg)
            print(f"Checked {site}: {msg}")

        time.sleep(60)