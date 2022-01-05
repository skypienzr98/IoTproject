
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

    # For POST requests, show the data
    if request.method == 'POST':
        clcount += 1
        # app.logger.info(request.form)  
        capLevel = int(request.form.get('capacity'))
        print()
        return render_template('base.html')
    
    # For GET requests, show the global capLevel variable value passed to template
    # app.logger.info("During GET request, capLevel=" + str(capLevel)) 
    print()
    return render_template('base.html')

@app.context_processor
def injectSensorData():
    global capLevel
    # app.logger.info("injectSensorData ran. Pass capLevel = " + str(capLevel))
    return dict(capLevel = int(capLevel))


# Background updater thread that runs before 1st client connects
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
    port = os.environ.get("PORT", 5000)              # Get port number of env at runtime, else use default port 5000
    app.run(debug=False, host='0.0.0.0', port=port)  # 0.0.0.0 port forwarding resolves the host IP address at runtime