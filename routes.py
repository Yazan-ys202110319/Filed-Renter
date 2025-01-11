from flask import render_template
import app

@app.route('/')
def home():
    return render_template('templates/index.html')