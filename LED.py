import RPi.GPIO as GPIO
import time

class LED:
    def __init__(self, pin):
        GPIO.setmode(GPIO.BCM)
        self.pin = pin

    def setup(self):
        GPIO.setup(self.pin, GPIO.OUT, initial=GPIO.LOW)

    def on(self):
       GPIO.output(self.pin, GPIO.HIGH) 

    def off(self):
       GPIO.output(self.pin, GPIO.LOW)
    
    def blink(self):
        while True:
            self.on()
            time.sleep(0.5)
            self.off()
            time.sleep(0.5)

    def destroy(self):
        GPIO.output(self.pin, GPIO.HIGH)
        GPIO.cleanup()

# led = LED(23)
# if __name__ == '__main__':
#     led.setup()
#     try:
#         led.blink()
#     # When 'Ctrl+C' is pressed, the program destroy() will be  executed.
#     except KeyboardInterrupt:
#         led.destroy()
