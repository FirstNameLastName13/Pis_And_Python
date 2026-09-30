import time
import board
import adafruit_dht
from datetime import datetime
from gpiozero import LED
from time import sleep

sensor = adafruit_dht.DHT11(board.D16) # Change the pin number to the data pin of your DHT11 import time
import board
import adafruit_dht
from datetime import datetime
from gpiozero import LED
from time import sleep

sensor = adafruit_dht.DHT11(board.D16) # Change the pin number to the data pin of your DHT11 
red = LED(21)
blue = LED(26)
print("time,celsius,fahrenheit")

def to_fahrenheit(c):
    f = (c * 9/5) + 32
    return f 

while True:
    try:
        celsius = sensor.temperature # Get the temperature in Celcius from the sensor
        fahrenheit = to_fahrenheit(celsius)
        current_time = datetime.now()
        
        text = ("{0},{1:0.1f},{2:0.1f} \n".format(current_time.strftime("%H:%M:%S"), celsius, fahrenheit))
        print(text)
        with open("temperature.csv", "a") as f:
            f.write(text)


        if fahrenheit >= 72:
            blue.off()
            red.on()
            time.sleep(3.0)
        if fahrenheit < 72:
            red.off()
            blue.on()
            time.sleep(3.0)
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        sensor.exit()
        raise error    
red = LED(21)
blue = LED(26)
print("time,celsius,fahrenheit")

def to_fahrenheit(c):
    f = (c * 9/5) + 32
    return f 

while True:
    try:
        celsius = sensor.temperature # Get the temperature in Celcius from the sensor
        fahrenheit = to_fahrenheit(celsius)
        current_time = datetime.now()
        
        text = ("{0},{1:0.1f},{2:0.1f} \n".format(current_time.strftime("%H:%M:%S"), celsius, fahrenheit))
        print(text)
        with open("temperature.csv", "a") as f:
            f.write(text)


        if fahrenheit >= 72:
            blue.off()
            red.on()
            time.sleep(3.0)
        if fahrenheit < 72:
            red.off()
            blue.on()
            time.sleep(3.0)
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        sensor.exit()
        raise error    
