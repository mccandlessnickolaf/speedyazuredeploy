from flask import Flask, redirect
app = Flask(__name__)

@app.route("/")
def hello():
    return redirect("https://script.google.com/macros/s/AKfycbw-1hn9B1UdpyqDk-81ME47fNzc9e2Gq_bPjNRtNPoAnrYyUUCf/exec", code=302)
