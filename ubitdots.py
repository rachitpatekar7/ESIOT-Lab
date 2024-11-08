import time
import requests
import math
import random
import Adafruit_DHT as dht
#TOKEN = "BBTR-CajzYXTtXV9iG8vXTJrWXsQDgbLAyi"
TOKEN = "BBUS-ABaxkcVDcBWOtHt7y7TQvknf7u9rzi"

DEVICE_LABEL = "Device1AJ"  # Put your device label here 
VARIABLE_LABEL_1 = "temperature"  # Put your first variable label here

def build_payload(variable_1):
    # REading sensor data
    humi, temp = dht.read_retry(dht.DHT22,18)
    payload = {variable_1: temp}
    return payload

def post_request(payload):
    # Creates the headers for the HTTP requests
    url = "http://industrial.api.ubidots.com"
    url = "{}/api/v1.6/devices/{}".format(url, DEVICE_LABEL)
    headers = {"X-Auth-Token": TOKEN, "Content-Type": "application/json"}

    # Makes the HTTP requests
    status = 400
    attempts = 0
    while status >= 400 and attempts <= 5:
        req = requests.post(url=url, headers=headers, json=payload)
        status = req.status_code
        attempts += 1
        time.sleep(4)

    # Processes results
    print(req.status_code, req.json())
    if status >= 400:
        print("[ERROR] Could not send data after 5 attempts, please check \
            your token credentials and internet connection")
        return False

    print("[INFO] request made properly, Samples uploaded successfully")
    return True


def main():
    payload = build_payload(VARIABLE_LABEL_1)
    print("[INFO] Attemping to send data")
    post_request(payload)
    print("[INFO] finished")

if __name__ == '__main__':
    while (True):
        main()
        time.sleep(2)
