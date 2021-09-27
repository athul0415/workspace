from flask import Flask
from flask_classful import FlaskView

app = Flask(__name__)

class TestView(FlaskView):

    def index(self):
    # http://localhost:8000/
        return "Welcome to Airbus"

TestView.register(app,route_base = '/')

if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = 8000, debug = True)
