from flask import Flask, render_template
from db import db
from constants import DATABASE

def create_app():
    app = Flask(__name__)
    app.config['DATABASE'] = DATABASE

    db.init_app(app)

    return app
    
app = create_app()


@app.route("/")
def map_stuff():
    database = db.get_db()

    stuff = database.execute("SELECT * FROM sites")
    sites_json = db.to_json(stuff)

    return render_template('index.html', sites=sites_json)