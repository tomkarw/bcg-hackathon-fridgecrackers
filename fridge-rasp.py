import time

import RPi.GPIO as GPIO
import dht11

MAX_TEMP = 10

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 14
dht = dht11.DHT11(pin = 21)

temp_list = [0 for _ in range(10)]

def run():
    while True:
        result = dht.read()
        
        if result.is_valid():
            print("Temperature: %-3.1f C" % result.temperature)
            print("Humidity: %-3.1f %%" % result.humidity)
    
            if result.temperature > all([temp > MAX_TEMP for temp in temp_list]):
                alert(result)
               
            temp_list.append(result)
            temp_list.pop(0)
            print(temp_list)
            time.sleep(60)
        else:
            print("Error: %d" % result.error_code)
    
def alert(result):
    print(f"ALERT!: temprerature {result.temperature} is above the threshold of {MAX_TEMP}")

if __name__ == "__main__":
    run()