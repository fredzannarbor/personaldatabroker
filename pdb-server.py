#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import logging
import psutil
import subprocess
import os
#import yaml
#import ipaddress when used with stats

from flask import Flask, jsonify

from two1.wallet.two1_wallet import Wallet
from two1.bitserv.flask import Payment


app = Flask(__name__)

# setup wallet
wallet = Wallet()
payment = Payment(app, wallet)

# hide logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.WARNING)


@app.route('/buy/basics')
@payment.required(3000)
def basics():

    with open('static/basics.json', 'r') as f:
        data = json.load(f)
        return jsonify(data)

@app.route('/buy/all')
@payment.required(100000)
def all():

    with open('static/all.json', 'r') as f:
        data = json.load(f)
        return jsonify(data)

# for non prototype, make this a database

@app.route('/buy/interests')
@payment.required(3000)
def BISACs():

    with open('static/myinterests', 'r') as f:
        data = json.load(f)
        return jsonify(data)

@app.route('/buy/iabs')
@payment.required(5000)
def iabs():

    with open('static/myiabs.json', 'r') as f:
        data = json.load(f)
        return jsonify(data)

@app.route('/buy/myersbriggs')
@payment.required(5000)
def myersbriggs():
    with open('static/myersbriggs.json', 'r') as f:
        data = json.load(f)
        return jsonify(data)

@app.route('/buy/ocean')
@payment.required(5000)
def fivefactors():
    with open('static/ocean.json', 'r') as f:
        data = json.load(f)
        return jsonify(data)

@app.route('/buy/contact')
@payment.required(10000)
def person():

    with open('static/contact.json', 'r') as f:
        data = json.load(f)
        return jsonify(data)

@app.route('/buy/besthours')
@payment.required(20000)
def besthours():

    with open('static/besthours.json', 'r') as f:
        data = json.load(f)
        return jsonify(data)

@app.route('/buy/for21')
@payment.required(3000)
def for21():

    with open('static/for21.json', 'r') as f:
        data = json.load(f)
        return jsonify(data)

if __name__ == '__main__':
    import click

    @click.command()
    @click.option("-d", "--daemon", default=False, is_flag=True,
                  help="Run in daemon mode.")
    def run(daemon):
        if daemon:
            pid_file = './pdb.pid'
            if os.path.isfile(pid_file):
                pid = int(open(pid_file).read())
                os.remove(pid_file)
                try:
                    p = psutil.Process(pid)
                    p.terminate()
                except:
                    pass
            try:
                p = subprocess.Popen(['python3', 'pdb-server.py'])
                open(pid_file, 'w').write(str(p.pid))
            except subprocess.CalledProcessError:
                raise ValueError("error starting pdb-server.py daemon")
        else:
            print("Personal marketing broker running on port 5014...")
            app.run(host='::', port=5014, debug=True)

    run()
