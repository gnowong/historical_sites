# Historical Sites

Written in Python and JavaScript/TypeScript, a simple web app displaying UNESCO world heritage sites from a sqlite database.

## Setup

Install flask via pip (`pip install Flask`). It is recommended to use a python virtual environment.

Download the leaflet files from https://leafletjs.com/download.html. Currently they are expected to be placed in the `flaskr/static` directory. Unzip them there.

When those files are placed, inside the `flaskr/` directory, run `flask init-db`. This will create the database.

When you are ready, run `flask run` inside the `flaskr/` directory.