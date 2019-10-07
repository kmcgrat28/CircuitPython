import time
import board
import digitalio

switch = digitalio.DigitalInOut(board.D8)
switch.direction = digitalio.Direction.INPUT
switch.pull = digitalio.Pull.UP


from lcd.lcd import CursorMode

counter = 0
lastbutton = True
while True:
    time.sleep(.05)
    if switch.value
        counter = counter + 1

    if  not switch.value and lastbutton:

    lastbutton = switch.value