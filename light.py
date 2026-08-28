from gpiozero import LED
from time import sleep

blue = LED(18)

while True:
    blue.on()
    sleep(1)
    blue.off()
    sleep(1)
