from flask import render_template,session,request,abort,Response,jsonify
from TravelCompanion import app

@app.route('/')
@app.route('/home')
def home():
    return 'Flask App'