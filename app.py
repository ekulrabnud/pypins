from flask import Flask
from pins import *

rpi = RPiRelay()

app = Flask(__name__)

@app.route("/")
def relay():
	rpi.get_pinstate_all()

    

if __name__ == "__main__":
    app.run(host='0.0.0.0')