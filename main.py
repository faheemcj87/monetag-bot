
import requests
import random
import time

# Monetag link
URL = "https://stenexeb.xyz/4/9178234"

# Proxy config
PROXY = {
    "http": "http://faheemcj-zone-resi:Stranger786@7f557e171ddee596.nbd.us.ip2world.vip:6001",
    "https": "http://faheemcj-zone-resi:Stranger786@7f557e171ddee596.nbd.us.ip2world.vip:6001"
}

# Random user agents
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)",
    "Mozilla/5.0 (Linux; Android 10; SM-G975F)"
]

def generate_traffic():
    while True:
        headers = {
            "User-Agent": random.choice(USER_AGENTS)
        }
        try:
            response = requests.get(URL, headers=headers, proxies=PROXY, timeout=10)
            print(f"Visited: {URL} - Status: {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")
        time.sleep(random.randint(15, 30))

if __name__ == "__main__":
    generate_traffic()
