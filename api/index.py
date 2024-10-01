from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/')
def home():
    return subprocess.getoutput("""echo "$(ls . | tr "\n" " " )||$(pwd)||$(ls .. | tr "\n" " ")"""")

@app.route('/about')
def about():
    return 'About'
