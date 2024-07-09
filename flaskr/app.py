from flask import Flask, render_template
from db import db
from constants import DATABASE
import csv
import sqlite3

def create_app():
    app = Flask(__name__)
    app.config['DATABASE'] = DATABASE

    db.init_app(app)

    return app
    
app = create_app()


@app.route("/")
def map_stuff():
    database = db.get_db()
    return render_template('index.html', sites=["o"]) 