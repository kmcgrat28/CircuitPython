import pulseio
import board
import analogio

led = analogio.AnalogOut(board.A0)
brightness = 40000
fadeAmount = 10

import time

while True:
    led.value = brightness
    brightness = brightness + fadeAmount

    if brightness <= 40000 or brightness >= 65000:
      fadeAmount = -fadeAmount