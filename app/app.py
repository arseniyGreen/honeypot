from flask import Flask
from flask import request
from flask import jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "You've fucked up. I've got your ip: " request.environ.get('HTTP_X_REAL_IP', request.remote_addr)

if __name__ == "__main__":
    app.run(debug=True)
