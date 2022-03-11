import RPi.GPIO as GPIO
import dht11 
import time
import datetime
import csv

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 14
instance = dht11.DHT11(pin=14)

def write_csv(t, h):
    with open('Data_2_24.csv', 'a') as f:
        n = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
        f.write(str(n) + "," +  str(t) + "," + str(h) + "\n")

try:
	while True:
	    result = instance.read()
	    if result.is_valid():
	        write_csv(result.temperature, result.humidity)
	        print("Tem: %-3.1f C" % result.temperature)
	        print("Hum: %-3.1f %%" % result.humidity)

	    time.sleep(3)

except KeyboardInterrupt:
    GPIO.cleanup()