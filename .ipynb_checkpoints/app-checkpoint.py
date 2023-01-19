#Import Dependencies
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#Setup Database
#engine = create_engine("SQL_FILE_LOCATION")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(autoload_with = engine)

# View all of the classes that automap found
Base.classes.keys()

# Save references to the table(s) based on previous step
#x = Base.classes.x

#SET UP FLASK
# Create an app
app = Flask(__name__)

# Flask Routes
@app.route("/")
def welcome():
    """List all available api routes."""
    return ()

@app.route("PLACEHOLDER_TEXT")
def names():
    # Create our session (link) from Python to the DB
    session = Session(engine)

if __name__ == '__main__':
    app.run(debug=True)
