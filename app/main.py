from flask import Flask, render_template, request, url_for, redirect, jsonify, Response
from flask.json import loads
from time import sleep, localtime, strftime
from datetime import datetime
from pytz import timezone
import os
import logging 
from turbo_flask import Turbo
import threading
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy import create_engine
import json
from random import random
import time

# ---------------------------------------

logging.basicConfig(level=logging.DEBUG)

app = Flask(__name__)
turbo = Turbo(app)

capLevel = 0
turbocount = 0
clcount = 0

# CHANGE to 'dev' when developing locally, 'prod' when deploying
ENV = 'dev'
if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:[Your Password]@localhost/[database name]'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://qaauaxtosvtcxc:b0029591cf5c7893d9f01d997c0b2210932aaba7a64459e5e08e08be57f7efcc@ec2-54-83-21-198.compute-1.amazonaws.com:5432/d1vhc63t8ojb7o'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#----------------------------------

class App_User(db.Model):

    __tablename__ = 'app_user'
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(255), nullable=False)
    email=db.Column(db.String(255), nullable=False)
    readingss = db.relationship('Sensor_Log', backref=db.backref('app_user',lazy=True))

    def __init__(self,name,email):
        self.name=name
        self.email=email

class Sensor_Log(db.Model):

    __tablename__ = 'sensor_log'
    id=db.Column(db.Integer,primary_key=True)
    capLevel=db.Column(db.Integer, nullable=False)
    reading_time=db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    app_user_id=db.Column(db.Integer,db.ForeignKey('app_user.id'),nullable=False)

    def __init__(self, capLevel, reading_time, app_user_id):
        self.capLevel = capLevel
        self.reading_time = reading_time
        self.app_user_id = app_user_id

#Migrate(app, db)
#------------------------------------------------------------------------------------------------------

# Home page (Dashboard)
@app.route("/", methods=['GET'])
def home():
    return render_template('index.html')

@app.route('/submit', methods=['GET','POST'])
def submit():
  name= request.form['name']
  email=request.form['email']
  
  user = App_User(name,email)
  db.session.add(user)
  db.session.commit()

  return redirect('/log_Data')

@app.route('/log_Data', methods=['GET','POST'])
def log_Data():
    global capLevel
    global time

    if request.method == 'POST':
        # app.logger.info(request.form)  
        capLevel= request.form.get('capacity')
        newlog = Sensor_Log(
        capLevel= request.form.get('capacity'),  
        reading_time = datetime.now(tz=timezone('Asia/Kuala_Lumpur')),
        app_user_id = 1
        )
        
        db.session.add(newlog)
        db.session.commit()        
	
        ##return "data logged"
        
    return render_template('base.html', capLevel=capLevel,time=time)

@app.route('/data', methods=["GET", "POST"])
def data():    
    if request.method == 'GET':
        Capacity = capLevel
        data = [time() * 1000, Capacity]

        response = make_response(json.dumps(data))

        response.content_type = 'application/json'

        return response    

@app.route('/cap-data')
def cap_data():
    def generate_cap_data():
        while True:
            json_data = json.dumps(
                {'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'), 'value': capLevel})
            yield f"data:{json_data}\n\n"
            time.sleep(1)

    return Response(generate_cap_data(), mimetype='text/event-stream')   

@app.context_processor
def injectSensorData():
    global capLevel    
        
    return dict(
    capacity = capLevel
    )

#----------------------------------------------------------------------------

#------------------------------------------------------------------------------
# Background updater thread that runs before 1st client connects
@app.before_first_request
def create_tables():
    db.create_all()

def before_first_request():
    threading.Thread(target=update_sensor_data).start()

def update_sensor_data():
    with app.app_context():    
        while True:
            sleep(5)
            turbo.push(turbo.replace(render_template('base.html'), 'base'))
            
#-----------------------------------------------------------------------

if __name__ == '__main__':
    port = os.environ.get("PORT", 5000)# Get port number of env at runtime, else use default port 5000
    app.run(debug=True, host='0.0.0.0', port=port)  # 0.0.0.0 port forwarding resolves the host IP address at runtime