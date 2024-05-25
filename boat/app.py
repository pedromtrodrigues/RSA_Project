import json
import paho.mqtt.client as mqtt
import threading
from time import sleep
import os

boat_id = os.getenv('BOAT_ID')

def main():
    #generate()
    while True:
        print(f"Boat{boat_id} is running...")
        sleep(10)

if __name__ == "__main__":
    main()