# Python Script To Control Garage Door

# Load libraries
import RPi.GPIO as GPIO
import time
from bottle import route, run, template, redirect

# Set up the GPIO pins
GPIO.setmode(GPIO.BOARD)
pin=11
GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, False)   

if False:
	GPIO.output(pin, True)
	time.sleep(.8)
	GPIO.output(pin, False)
	time.sleep(.8)
	GPIO.output(pin, True)
	time.sleep(.8)
	GPIO.output(pin, False)
	time.sleep(.8)
# Handle http requests to the root address
@route('/')
def index():
 return 'Go away.'

# Handle http requests to /garagedoor
@route('/garagedoor/:doornum/cycled')
def garagedoor(doornum=0):
 if doornum == '0':
   return 'No door number specified'
 return 'Door number {} cycled.'.format(doornum)

# Handle http requests to /garagedoor
@route('/garagedoor/:doornum')
def garagedoor(doornum=0):
 if doornum == '0':
   return 'No door number specified'

 elif doornum == '1':
   GPIO.output(pin, True)
   time.sleep(.8)
   GPIO.output(pin, False)
   redirect("/garagedoor/{}/cycled".format(doornum))
 return 'Go away!'

try:
  run(host='0.0.0.0', port=1234)
except:
  GPIO.cleanup()
  print("Done")
