import flask
from flask import Flask, render_template, Response, redirect, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return "Szerver fut"

if __name__ == "__main__":
    app.run('0.0.0.0', 3000)