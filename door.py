# Python Script To Control Garage Door

# Load libraries
try:
  import RPi.GPIO as GPIO
except ModuleNotFoundError:
  import fake_gpio as GPIO

import time
from bottle import route, run, view, redirect, request, post

# Set up the GPIO pins
GPIO.setmode(GPIO.BOARD)
pin=11
GPIO.setup(pin, GPIO.OUT)
GPIO.output(pin, False)   

# Handle http requests to the root address
@route('/')
def index():
 return redirect("/garagedoor/1")

@route('/garagedoor/<doornum>/<cycled>')
@route('/garagedoor/<doornum>')
@view('./door.html')
def garagedoor(doornum=0, cycled=False):
  return dict(doornum=doornum,
              cycled=cycled)

# Handle http requests to /garagedoor
@post('/garagedoor/<doornum>')
def garagedoor(doornum=0):
 if doornum == '0':
   return 'No door number specified'

 elif doornum == '1':
   GPIO.output(pin, True)
   time.sleep(.8)
   GPIO.output(pin, False)
   redirect("/garagedoor/{}/cycled".format(doornum))
 return 'Go away!'

if __name__ == '__main__':
    try:
      run(host='0.0.0.0', port=1234)
    finally:
      GPIO.cleanup()
      print("Done")
