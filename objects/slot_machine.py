from gpiozero import LED
from time import sleep
import tm1637
from gpiozero import Button
import random

# Creating 4-digit 7-segment display object
display = tm1637.TM1637(clk=24, dio=25)  # Using GPIO pins 24 and 25
clear = [0, 0, 0, 0]

button = Button(6)
cheater = Button(12)
led = LED(18)

def numbers():
    #picks 4 random numbers between 0 and 9 (inclusive) and returns them
    a = random.randint(0,9)
    b = random.randint(0,9)
    c = random.randint(0,9)
    d = random.randint(0,9)
    global x
    x = str(a) + str(b) + str(c) + str(d)
    return x
def cheating_nums(y,z):
    #cheating_nums() basically picks a random range between 0 and 9 and then selects 4 numbers within that range
    #y is the start point of the range
    #x is the end point of the range
    
    #a,b,c,d are the random numbers
    a = random.randint(y,z)
    b = random.randint(y,z)
    c = random.randint(y,z)
    d = random.randint(y,z)
    global w
    w = str(a) + str(b) + str(c) + str(d)
    print(f"{y} - {z}")
    return w

while True:
    #if the player is cheating
    y = random.randint(0,4)
    z = random.randint(5,9)
    if button.is_pressed and cheater.is_pressed:
        display.show(cheating_nums(y,z))
        sleep(0.05)
        if w[0] == w[1] == w[2] == w[3]:
            led.on()
            sleep(5)
            led.off()
    #if the player isn't cheating
    elif button.is_pressed and not cheater.is_pressed:
        display.show(numbers())
        sleep(0.05)
        if x[0] == x[1] == x[2] == x[3]:
            led.on()
            sleep(5)
            led.off()
