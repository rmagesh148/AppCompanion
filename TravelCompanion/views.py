from flask import render_template,session,request,abort,Response,jsonify
from TravelCompanion import app
from TravelCompanion import models


@app.route('/')
def home():
    rec = models.Airport.query.all()
    print('*'*100)
    print(rec)
    return jsonify([r.serialize() for r in rec])