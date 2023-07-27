#!/usr/bin/env python3

import RPi.GPIO as GPIO
import os
from http.server import BaseHTTPRequestHandler, HTTPServer

host_name = '192.168.1.29'
host_port = 8000

def setupGPIO():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(21, GPIO.OUT)

class MyServer(BaseHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers

    def _redirect(self, path):
        self._response(303)
        self.send_header('Content-type', 'text/html')
        self.send_header('Location', path)
        self.end_headers

    def do_GET(self):
        

def controlLED():
    try:
        while True:
            user_input = input(
                    "Turn LED On or Off:")
            if user_input == "1":
                GPIO.output(21, GPIO.HIGH)
                print("LED is on")
            elif user_input == "0":
                GPIO.output(21, GPIO.LOW)
                print("LED is off")
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("")


setupGPIO()
controlLED()
