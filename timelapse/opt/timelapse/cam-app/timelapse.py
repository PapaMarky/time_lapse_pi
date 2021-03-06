from flask import Flask
from flask import render_template
from flask import request

import json
import subprocess

from time import sleep

app = Flask(__name__)

def snapshot(br="50", rot="false", ex="off", awb="off", sh="0", co="0", sa="0", ifx="none", t=1000):
        h = 480 # 240*1.5
        w = 640 # 320*1.5
        # roi = '-roi 0.68,0.5,0.25,0.25'
        roi = ''
        cmd = 'raspistill -n {} -h {} -w {} -rot {} -br {} -ex {} -awb {} -sh {} -co {} -sa {} -ifx {} -t {} -o /home/pi/cam-app/static/preview.png'.format(roi, h, w, rot, br, ex, awb, sh, co, sa, ifx, t)
        p = subprocess.run(cmd.split(), stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        print(p.stdout)
        return {'status': p.returncode, 'output': p.stdout.decode('utf-8'), 'command': cmd}

app = Flask(__name__)

@app.route('/')
def index():
        return render_template('index.html', preview='preview.png')

@app.route('/snapshot')
def take_snapshot():
        brightness = request.args.get('br')
        rot = request.args.get('rot')
        exposure = request.args.get('ex')
        awb = request.args.get('awb')
        sh = request.args.get('sh')
        co = request.args.get('co')
        sa = request.args.get('sa')
        ifx = request.args.get('ifx')
        status = snapshot(br=brightness, rot=rot, ex=exposure, awb=awb, sh=sh, co=co, sa=sa, ifx=ifx)
        return json.dumps(status)

if __name__ == '__main__':
        app.run(debug=True, host='0.0.0.0')
