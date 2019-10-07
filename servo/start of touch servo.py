import time
import board
import pulseio
from adafruit_motor import servo
import touchio

touch_pin = touchio.TouchIn(board.A1)
print(touch_pin1.value)
touch_pin = touchio.TouchIn(board.A4)
print(touch_pin2.value)

pwm = pulseio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

my_servo = servo.Servo(pwm)

while True:
   if touch_pin1.value:
       for angle in range(0, 180, 5):
           my_servo.angle = angle
           time.sleep(0.1)

    if touch_pin2.value:
               for angle in range(180, 0, -5)
               my_servo.angle = angle
               time.sleep(0.1)
