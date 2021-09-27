from flask import Flask 
from flask_classful import FlaskView
 
app = Flask(_name_) 

class TestView(FlaskView): 
    def index(self):                                       
         return "Welcome to Airbus" 
		 
TestView.register(app,route_base = '/')

if _name_ == '_main_':    
   app.run(host ='0.0.0.0', port = 8000, debug = True)
