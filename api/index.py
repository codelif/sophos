from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def home():
    with open("sophos_script_py") as f:
        return Response(f.read(), mimetype="text/plain")

@app.route('/about')
def about():
    return 'About'
