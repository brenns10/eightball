#!/usr/bin/env python3
import random

from flask import Flask, after_this_request, send_file
app = Flask(__name__)

@app.route("/eightball.gif")
def eightball():
    @after_this_request
    def add_cache_control_no_cache(response):
        response.headers['Cache-control'] = 'no-cache'
        return response
    filename = "img/%d.gif"
    return send_file(filename % random.randint(1, 20))
