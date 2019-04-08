import RPi.GPIO as GPIO
import time

def servoPos():
    #print("starting")
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11,GPIO.OUT)
    GPIO.setup(12,GPIO.OUT)
    #print("setup complete")
    pwm1 = GPIO.PWM(11,50)
    pwm2 = GPIO.PWM(12,50)
    pulseWidth = 0.001
    frequency = 50
    dutyCycle = pulseWidth*frequency
    #print("beginning cycle")
    pwm1.start(5)
    time.sleep(2)
    pwm1.ChangeDutyCycle(10)
    time.sleep(0.1)
    pwm1.ChangeDutyCycle(0)
    time.sleep(1)
    
    pwm2.start(5)
    time.sleep(2)
    pwm2.ChangeDutyCycle(10)
    time.sleep(0.1)
    pwm2.ChangeDutyCycle(0)
    time.sleep(1)
    
    return

servoPos()