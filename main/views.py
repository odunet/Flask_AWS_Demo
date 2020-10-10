from flask import render_template
from main import app
#from main import db

@app.route('/')
def home():
    return render_template('home.html')
