from gpiozero import PWMLED
from time import sleep
from gpiozero import RotaryEncoder

rotor = RotaryEncoder(23, 18, wrap=True, max_steps=180) 
led = PWMLED(17)

while True:
    led.value = ((rotor.steps / 180) ** 2)
    print(rotor.steps, "-->", led.value)
    sleep(0.05)
