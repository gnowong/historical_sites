import sqlite3
import csv
import click
from flask import g, current_app
from constants import CSV_FILE


def read_csv():
    with open(CSV_FILE) as file:
        reader = csv.reader(file)
        for row in reader:
            print(row)

def init_db():
    db = get_db()

    with current_app.open_resource('db/schema.sql') as schema:
        db.executescript(schema.read().decode('utf8'))


@click.command('init-db')
def init_db_command():
    """Clear database and/or create tables"""
    init_db()
    click.echo("Database intialized")


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(current_app.config['DATABASE'])
        g.db.row_factory = sqlite3.Row
    
    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_app(app):
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)