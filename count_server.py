import os
import datetime
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import DateTime
import config

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__) 
app.config["SQLALCHEMY_DATABASE_URI"] = config.DATABASE_CONNECTION_URI#os.environ.get("DATABASE_URL") or "sqlite:///" + os.path.join(basedir, "data.sqlite")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]=False

db = SQLAlchemy(app)

class Connection(db.Model):
    __tablename__ = "connections"
    id = db.Column(db.Integer, primary_key=True)
    created_date = db.Column(DateTime, default=datetime.datetime.utcnow)

@app.errorhandler(404)
def page_not_found(e):
    return "<h1>Page not found Error 404</h1>"

@app.errorhandler(500)
def internal_server_error(e):
    return "<h1>Internal Server Error 500</h1>"

@app.route("/")
def index():
    connection = Connection() 
    db.session.add(connection)
    db.session.commit()
    return "<h1>I am counting this visit</h1>"


@app.route( '/view_counter/', methods=['GET'])
def view_counter():
    return  "Connections count: "+str(db.session.query(Connection).count())

if __name__ == '__main__':
    db.create_all()
    app.run(debug=False, host='0.0.0.0')