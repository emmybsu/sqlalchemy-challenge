# 1. Import Flask
import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
measurement = Base.classes.measurement
station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


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
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )


@app.route("/api/v1.0/precipitation")
def prcp():
    """Convert the query results to a dictionary using `date` as the key and `prcp` as the value.
    Return the JSON representation of your dictionary."""
    # session = Session(engine)

    # recent_date = session.query(measurement.date)
    # '''.\
    #     filter(measurement.date ==session.query(func.max(measurement.date))).\
    #     first()'''
    # recent_date
    # session.close()





# @app.route("/api/v1.0/stations")
# def stations():
#     """Return a JSON list of stations from the dataset."""



# @app.route("/api/v1.0/tobs")
# def tobs():
#     """Query the dates and temperature observations of the most active station for the last year of data.
#     Return a JSON list of temperature observations (TOBS) for the previous year."""


# @app.route("/api/v1.0/<start><br/>")
# def start():
#     """* Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
#   * When given the start only, calculate `TMIN`, `TAVG`, and `TMAX` for all dates greater than and equal to the start date."""


# @app.route("/api/v1.0/<start>/<end>")
# def start_end():
#     """* Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
#   * When given the start and the end date, calculate the `TMIN`, `TAVG`, and `TMAX` for dates between the start and end date inclusive."""



# 4. Define main behavior
if __name__ == "__main__":
    app.run(debug=True)
