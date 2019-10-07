import time
import board
import digitalio

switch = digitalio.DigitalInOut(board.D8)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP


interruptcount = 0
lastbutton = True
while True:
    print("the number of the interrupts is")
    time.sleep(.05)
    if switch.value:
        interruptcount = interruptcount + 1
        print(str(interruptcount  ))
photoIndicate = photo.value