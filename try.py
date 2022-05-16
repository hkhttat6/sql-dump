import os
import re
import subprocess
import time
import sys
import random
import requests
from subprocess import Popen , PIPE
from _thread import *
import threading
md=os.getcwd()
def p():
    os.chdir(md)
    try:
        p=open(os.getcwd()+"\\google.html", encoding='utf-8').readlines()
    except:
        p='nnn'
    return p
src='/recaptcha/api.js'
print(src in p)