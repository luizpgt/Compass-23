import sys 
import os, re, time
from datetime import datetime
import hashlib

def get_hash(key):
    try:
        h = hashlib.new('sha256', usedforsecurity=False)
        h.update(key.encode("utf-8"))
        return h.hexdigest()
    except:
        raise Exception('generate hash from message')

def get_timestamp():
    try:
        os.environ['TZ'] = 'America/Sao_Paulo'
        time.tzset()
        return time.strftime('%d-%m-%Y %H:%M:%S')
    except:
        raise Exception('get current timestamp')

def rm_extra_whitesp(message):
    try:
        return re.sub('\s+', ' ', message.strip())
    except:
        raise Exception('remove whitespaces from given string')

def fmt_message(msg):
    try: 
        return rm_extra_whitesp(msg.lower())
    except:
        raise Exception('properly format given string')