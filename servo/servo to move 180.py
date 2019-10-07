import time
import board
import pulseio
from adafruit_motor import servo
import touchio

touch_pin1 = touchio.TouchIn(board.A1)
print(touch_pin1.value)
touch_pin2 = touchio.TouchIn(board.A4)
print(touch_pin2.value)

pwm = pulseio.PWMOut(board.A3, duty_cycle=2 ** 15, frequency=50)

my_servo = servo.Servo(pwm)

my_servo.angle = 90
while True:
   if touch_pin1.value:
         if my_servo.angle >=2:
            my_servo.angle -= 1
            time.sleep(0.01)

   if touch_pin2.value:
         if my_servo.angle <=179:
            my_servo.angle += 1
            time.sleep(0.01)