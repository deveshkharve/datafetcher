# logger to log information
# logs data with the timestamp and levels
import logging
import os
import datetime
import config as CONFIG
import re
import time
import json
from flask import make_response, session
LOG_FILE_DIRECTORY = CONFIG.LOG_FILE_DIRECTORY

if not os.path.exists(LOG_FILE_DIRECTORY):
    os.makedirs(LOG_FILE_DIRECTORY)

# Set File and Format for logging

currDate = datetime.datetime.today().strftime('%Y-%m-%d')
logFilename = CONFIG.NAME + currDate + ".log"
logFilename = os.path.join(LOG_FILE_DIRECTORY, logFilename)
FORMAT = '%(asctime)s %(name)-12s %(levelname)s [%(pathname)s:%(lineno)d]: %(message)s'

logging.basicConfig(filename=logFilename, level=logging.DEBUG, format=FORMAT)

logger = logging.getLogger(CONFIG.NAME)
console = logging.StreamHandler()
console.setLevel(logging.DEBUG)
formatter = logging.Formatter(FORMAT)
console.setFormatter(formatter)
logger.addHandler(console)
logging.basicConfig(filename=logFilename, level=logging.DEBUG, format=FORMAT)

retryCount = 5
indexMap = {}

def xstr(s):
    if s is None:
        return ''
    return str(s)

def getDateFromLong(longDateTime):
    timeStr = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(longDateTime)))
    return timeStr

def root_dir():
    """ Returns root director for this project """
    return os.path.dirname(os.path.realpath(__file__ + '/..'))

def nice_json(arg):
    response = make_response(json.dumps(arg, sort_keys=True, indent=4))
    response.headers['Content-type'] = "application/json"
    return response

def authenticated(json):
    """
    function to authenitcate the user.
    current implementation uses a simple check for access Token
    this can later be made into something more sophisticated
    """
    if json is not None and 'auth' in json and json['auth'] == CONFIG.ACCESS_TOKEN:
        return True
    return False


def getParentName(stack):
    if len(stack) >= 2:
        return stack[1].function
    return 'unknown'


def makeSession(user):
    session['userName'] = user['username']
    session['userId'] = user['id']
    session['logged_in'] = True
    return None


def hasSession():
    return session and session['logged_in']


def deleteSession():
    session['logged_in'] = False
    session['userName'] = None
    session['userName'] = None