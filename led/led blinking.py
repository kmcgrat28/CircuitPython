import board
import digitalio
import pulseio
from digitalio import DigitalInOut, Direction
pwm_leds = board.D0
pwm = pulseio.PWMOut(pwm_leds, frequency=1000, duty_cycle=0)

led = digitalio.DigitalInOut(board.A1)
led.direction = digitalio.Direction.OUTPUT
brightness = 0
fade_amount = 1285
counter = 0

while True:

   pwm.duty_cycle = brightness

    brightness = brightness + fade_amount

    print(brightness)
 if brightness <= 0:
        fade_amount = -fade_amount
        counter += 1
    elif brightness >= 65535:
        fade_amount = -fade_amount
        counter += 1

 digital_leds.value = True
   time.sleep(.015)
  digital_leds.value = False
   time.sleep(.015)

