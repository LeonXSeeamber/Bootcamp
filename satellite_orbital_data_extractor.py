import requests
import os

# Configuration for downloading TLE history of Landsat 8
IDENTITY = "24009604@gateshead.ac.uk"
PASSWORD = "24009604gatesheadacuk"
TLE_HISTORY_URL = (
    "https://www.space-track.org/basicspacedata/query/class/gp_history/"
    "NORAD_CAT_ID/39084/orderby/TLE_LINE1%20ASC/format/tle"
)
OUTPUT_FILE = "data/landsat8_tle_history.txt"
LOGIN_URL = "https://www.space-track.org/ajaxauth/login"

def download_tle_history():
    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)
    with requests.Session() as session:
        print("Logging in to Space-Track.org...")
        resp = session.post(LOGIN_URL, data={'identity': IDENTITY, 'password': PASSWORD})
        if resp.status_code != 200:
            print(f"Login failed: {resp.status_code}")
            return
        print("Login successful. Downloading TLE history...")
        tle_resp = session.get(TLE_HISTORY_URL)
        if tle_resp.status_code == 200:
            with open(OUTPUT_FILE, "w") as f:
                f.write(tle_resp.text)
            print(f"TLE history saved to '{OUTPUT_FILE}'.")
        else:
            print(f"Failed to download TLE history: {tle_resp.status_code}")

if __name__ == "__main__":
    download_tle_history()
