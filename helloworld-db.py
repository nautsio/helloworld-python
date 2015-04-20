#!/usr/bin/env python

from flask import Flask
from redis import Redis
import os
import logging
import logging.handlers

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def hello():
    try:
       redis.incr('hits')
       hits = redis.get('hits')
       app.logger.info("hello called %s times" % hits)
       return 'Hello World! I have been seen %s times.\n' % hits
    except Exception as e:
       app.logger.error(str(e))
       return "Hello World! Cannot tell you how many times I have been seen.\n\t(%s)\n" % str(e)

if __name__ == "__main__":
    if os.path.exists('/dev/log'):
      handler = logging.handlers.SysLogHandler(address = '/dev/log')
    else:
      handler = logging.handlers.SysLogHandler()
    handler.setLevel(logging.ERROR)
    app.logger.addHandler(handler)
    app.run(host="0.0.0.0", port=80, debug=True)
