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

temp = 0
humi = 0
cnt = 0
judge = False
t = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
"""
def temp_cal(t, rt):
    return t + rt
"""
def t_judge():
    if t == datetime.datetime.now().strftime("%Y/%m/%d %H:%M"):
        return True
    else:
        return False
    
judge = t_judge()

def write_csv(a):
    with open('2022_3.csv', 'a') as f:
        f.write(str(a) + "," + f'{temp:.1f}' + "," + f'{humi:.0f}' + "\n")
        f.close()
  
try:
	while True:
	    result = instance.read()
	    if result.is_valid():
                judge = t_judge()
                if judge == True:
                    cnt += 1
                    temp += result.temperature
                    humi += result.humidity
                    
                    print(cnt)
                    print(f'{temp:.1f}')
                    print(f'{humi:.0f}')
                    #print('{:.1f}'.format(temp))
                    #print('{:.0f}'.format(humi))
                    
                else:
                    temp = temp / cnt
                    humi = humi / cnt
                    write_csv(t)
                    
                    t = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")
                    judge = True
                    temp = 0
                    cnt = 0
                    
	    time.sleep(2)

except KeyboardInterrupt:
    GPIO.cleanup()
