from flask import Flask, render_template, url_for
from db import db
from constants import DATABASE

def create_app():
    app = Flask(__name__)
    app.config['DATABASE'] = DATABASE

    db.init_app(app)

    return app
    
app = create_app()


@app.route("/")
def map_sites():
    database = db.get_db()

    sites = database.execute("SELECT * FROM sites")
    sites_json = db.to_json(sites)
    for site in sites.fetchall():
        name = site["site_name"].replace(" ", "-")
        url_for("static", filename=f"site-images/{name}") # Add actual images

    return render_template('index.html', sites=sites_json)