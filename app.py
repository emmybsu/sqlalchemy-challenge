# 1. Import Flask
import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite", connect_args={'check_same_thread': False})

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
measurement = Base.classes.measurement
station = Base.classes.station

# Create session from Python to the DB
Session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
year_recent = '2016-08-23'

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/(**user to enter start date**)<start><br/>"
        f"/api/v1.0/(**user to enter start date and end date**)")


#################################################
# Queries
#################################################



@app.route("/api/v1.0/precipitation")
def precipitation():
    """Convert the query results to a dictionary using `date` as the key and `prcp` as the value.
    Return the JSON representation of your dictionary."""   
    results = Session.query(measurement.date, measurement.prcp, func.avg(measurement.prcp)).filter(measurement.date >= year_recent).group_by(measurement.date).all()              
    return jsonify(results)

@app.route("/api/v1.0/stations")
def stations():
    """Return a JSON list of stations from the dataset."""
    stations = Session.query(station.station).all()
    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def tobs():
    """Query the dates and temperature observations of the most active station for the last year of data.
    Return a JSON list of temperature observations (TOBS) for the previous year."""
    results = Session.query(measurement.date, measurement.tobs).filter(measurement.station == 'USC00519281').filter(measurement.date >= year_recent).all()
    return jsonify(results)


@app.route("/api/v1.0/<start>")
@app.route("/api/v1.0/<start>/<end>")
def sttenddates(start = '2016-08-23', end='2017-08-23'):
    """* Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
    * When given the start only or the start/end date, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date."""
    
    #SELECT Statement
    sel = [func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)]
    if not end:
        #calculate min, max, avg for dates greater than start
        results = Session.query(*sel).filter(measurement.date >= start).all()
    else:
        #calculate min, max, avg for dates between start and stop
        results = Session.query(*sel).filter(measurement.date >= start).filter(measurement.date <= end).all()
    
    #unravel results into a 1D array and convert to list
    temps = list(np.ravel(results))
    
    return jsonify(temps=temps)

# 4. Define main behavior
if __name__ == "__main__":
    app.run(debug=True)
