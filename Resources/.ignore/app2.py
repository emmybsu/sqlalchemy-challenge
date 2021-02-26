import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
measurement = Base.classes.measurement
station = Base.classes.station
session = Session(engine)
#################################################
# Flask Setup
#################################################
app = Flask(__name__)


# class Session(Base):
#     __tablename__ = 'sessions'

#     id = Column(Integer, primary_key=True)
#     token = Column(String(200))
#     user_id = Column(Integer, ForeignKey('app_users.id'))
#     user = relationship('model.user.User', back_populates='sessions')

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
        f"/api/v1.0/<start> and /api/v1.0/<start>/<end>"
    )


# @app.route("/api/v1.0/precipitation")
# def precipitation():
#     """Return a list of Dates and precipitation from last year"""
#     # Query Invoices for Billing Country
#     results = Session.query(measurement.date, measurement.prcp).\
#         filter(measurement.date <= '2017-12-31').\
#         filter(measurement.date >= '2017-01-01').all()

#     # Convert the query results into a dictionary using date as the key and precipitation as the value
#     all_prcp = []
#     for result in results:
#         prcp_dict = {}
#         prcp_dict["date"] = result[0]
#         prcp_dict["prcp"] = float(result[1])

#         all_prcp.append(prcp_dict)

#     return jsonify(all_prcp)
    
# # @app.route("/api/v1.0/stations")
# def stations():
#     """Return a list of weather stations from the dataset """
#     # Query all stations
#     results = Session.query(station.station).all()
    
#     stations_list = list(np.ravel(results))
    
#     return jsonify(stations_list)

# @app.route("/api/v1.0/tobs")
# def tobs():
#     """Return a list of temperature observations from the previous year """
#     # Query for all temperature observations from previous year
#     results = Session.query(measurement.date, measurement.tobs).\
#         group_by(measurement.date).\
#         filter(measurement.date <= '2017-12 31').\
#         filter(measurement.date >= '2017-01-01').all()

#     tobs_list = list(np.ravel(results))
#     return jsonify(tobs_list)

# @app.route("/api/v1.0/<start>")
# @app.route("/api/v1.0/<start>/<end>")
# def start_end(start=None, end=None):
#     """Return a list of min, avg, max for specific dates"""
#     sel = [func.min(measurement.tobs), func.avg(measurement.tobs), func.max(measurement.tobs)]
#     if not end:
#         results= Session.query(*sel).filter(measurement.date >= start).all()
#         temps = list(np.ravel(results))
#         return jsonify(temps)
    
#     results = Session.query(*sel).filter(measurement.date >= start).filter(measurement.date <= end).all()
#     temps2 = list(np.ravel(results))
#     return jsonify(temps2)

if __name__ == '__main__':
    app.run()