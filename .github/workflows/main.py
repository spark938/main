import time
import requests

def run():
    url = "https://nc-lotory.kesug.com/niyamitakelasa_browser_trigger.php"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/122.0.0.0 Safari/537.36"
    }
    while True:
        try:
            response = requests.get(url, headers=headers)
            print(f"[{time.ctime()}] Triggered: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(59)

if __name__ == "__main__":
    run()
