import time
import board
import digitalio

switch = digitalio.DigitalInOut(board.D8)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.DOWN

interruptcount = 0
lastbutton = True
while True:
    print("the number of the interrupts is")
    if not switch.value and lastbutton:
        interruptcount = interruptcount + 1
    if not switch.value and lastbutton:
        interruptcount = interruptcount - 1
        print(str(interruptcount  ))
    photoIndicate =  photo.value