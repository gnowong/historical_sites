import sqlite3
import csv
import click
import json
from flask import g, current_app
from constants import CSV_FILE

def dict_factory(cursor, row):
    fields = [column[0] for column in cursor.description]
    return {key: value for key, value in zip(fields, row)}


def to_json(crsr: sqlite3.Cursor):
    rows = crsr.fetchall()
    row_json = json.dumps(rows)
    
    return row_json


def read_csv():
    database = get_db()
    with open(CSV_FILE) as file:
        reader = csv.reader(file)
        for row in reader:
            database.cursor().execute("INSERT INTO sites (site_name, lon, lat) VALUES (?, ?, ?)", (row[0], row[1], row[2]))
        
        database.commit()

def init_db():
    click.echo("running init_db")
    db = get_db()

    with current_app.open_resource('db/schema.sql') as schema:
        db.executescript(schema.read().decode('utf8'))
    
    read_csv()
    


@click.command('init-db')
def init_db_command():
    """Clear database and/or create tables"""
    init_db()
    click.echo("Database intialized")


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(current_app.config['DATABASE'])
        g.db.row_factory = dict_factory
    
    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)