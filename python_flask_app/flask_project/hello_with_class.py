from flask import Flask, Response


class EndpointAction(object):

    def __init__(self, action):
        self.action = action
        self.response = Response(status=200, headers={})

    def __call__(self, *args):
        self.action()
        return self.response


class FlaskAppWrapper(object):
    app = None

    def __init__(self):
        self.app = Flask(__name__)

    def run(self):
        self.app.run(host ='0.0.0.0', port = 8000, debug = True)

    def add_endpoint(self, endpoint=None, endpoint_name=None, handler=None):
        self.app.add_url_rule(endpoint, endpoint_name, EndpointAction(handler))


def action():
    print ("inside action")
    return "Hello Airbus"

if __name__ == "__main__":
    a = FlaskAppWrapper()
    a.add_endpoint(endpoint='/abc', endpoint_name='abc', handler=action)
    a.run()
