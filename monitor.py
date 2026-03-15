import requests
import time
import os

SITES = os.getenv('SITES_TO_CHECK', "https://google.com,https://github.com").split(",")

STATUS_MESSAGES = {
    200: "The site is working great!",
    404: "Page not found (check the URL).",
    500: "Server error: it's down.",
    502: "Bad gateway (server is overloaded).",
    503: "Service temporarily unavailable."
}

def check_sites():
    print(f"---Starting check at {time.ctime()}---")
    
    for site in SITES:
        site = site.strip()
        try:
            # We visit the website and wait for a maximum of 5 seconds
            response = requests.get(site, timeout=5)
            # Take a code
            code = response.status_code
            # Output of pre-compiled code or uncompiled code
            message = STATUS_MESSAGES.get(code, f"An unusual response was received (Code: {code})")
            print(f"[{site}] - {message}")

        except Exception as e:
            print(f"[{site}] - ERROR: Unable to connect to the site. ({e})")

if __name__ == "__main__": # Monitoring will continue while the script is running
    while True:
        check_sites()
        time.sleep(60)