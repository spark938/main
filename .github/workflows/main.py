import time
import requests

def run():
    url = "https://nc-lotory.kesug.com/niyamitakelasa_browser_trigger.php"
    while True:
        print("Pinging the URL...")
        try:
            res = requests.get(url)
            print(f"Response: {res.status_code}")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(59)

if __name__ == "__main__":
    run()
