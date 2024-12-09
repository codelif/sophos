from flask import Flask, Response

app = Flask(__name__)

@app.route('/')
def yes():
    with open("sophos_script_py") as f:
        return Response(f.read(), mimetype="text/plain")
