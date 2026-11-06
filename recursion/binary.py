#importing relavent libraries
from gpiozero import LED
from time import sleep

red1 = LED(16)
red2 = LED(17)
red4 = LED(18)
red8 = LED(19)
red16 = LED(20)
red32 = LED(21)
red64 = LED(22)
red128 = LED(23)

def to_binary(n):
    if n == 0:
        return 0
    else:
        return (n % 2 + 10 * to_binary(n//2))

x = (input("enter a number between 1 - 255 (inclusive)"))

binary = (to_binary(int(x)))
print(binary)
binary = str(binary)

if len(binary) == 1:
    binary = "0000000" + binary
elif len(binary) == 2:
    binary = "000000" + binary
elif len(binary) == 3:
    binary = "00000" + binary
elif len(binary) == 4:
    binary = "0000" + binary
elif len(binary) == 5:
    binary = "000" + binary
elif len(binary) == 6:
    binary = "00" + binary
elif len(binary) == 7:
    binary = "0" + binary
else:
    binary = binary

if binary[0] == "1":
        red1.on()
else:
        red1.off()

if binary[1] == "1":
        red2.on()
else:
        red2.off()
    
if binary[2] == "1":
        red4.on()
else:
        red4.off()

if binary[3] == "1":
        red8.on()
else:
        red8.off()

if binary[4] == "1":
        red16.on()
else:
        red16.off()

if binary[5] == "1":
        red32.on()
else:
        red32.off()
    
if binary[6] == "1":
        red64.on()
else:
        red64.off()

if binary[7] == "1":
  
