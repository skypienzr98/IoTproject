
from flask import Flask
from flask import render_template, request, url_for
from time import sleep
import os
import logging 
from turbo_flask import Turbo
import threading

logging.basicConfig(level=logging.DEBUG)

capLevel = 0
turbocount = 0
clcount = 0

app = Flask(__name__)
turbo = Turbo(app)

@app.route("/", methods=['GET','POST'])
def home():
    global capLevel
    global clcount

    if request.method == 'POST':
        clcount += 1 
        capLevel = int(request.form.get('capacity'))
        print()
        return render_template('base.html')
    
    print()
    return render_template('base.html')

@app.context_processor
def injectSensorData():
    global capLevel
    return dict(capLevel = int(capLevel))


@app.before_first_request
def before_first_request():
    threading.Thread(target=update_sensor_data).start()

def update_sensor_data():
    global turbocount
    global clcount

    with app.app_context():    
        while True:
            sleep(30)
            app.logger.info("At turbo function #" + str(turbocount) + " now. It sees capLevel " + "#" + str(clcount) +" = " + str(capLevel))
            turbocount+=1
            turbo.push(turbo.replace(render_template('base.html'), 'base'))

if __name__ == '__main__':
    port = os.environ.get("PORT", 5000)              
    app.run(debug=False, host='0.0.0.0', port=port)  