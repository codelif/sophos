from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    with open("sophos_script_py") as f:
        return f.read()

@app.route('/about')
def about():
    return 'About'
