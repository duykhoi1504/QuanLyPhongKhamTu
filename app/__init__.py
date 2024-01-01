from flask import Flask
from urllib.parse import quote
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager


app=Flask(__name__)

app.secret_key="Admin@123456789"
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql+pymysql://root:%s@localhost/clinicdb1' % quote('Admin@123')
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
app.config["PAGE_SIZE"]=6


db = SQLAlchemy(app)
login = LoginManager(app=app)

import cloudinary

cloudinary.config(
    cloud_name="dx5nqi4ll",
    api_key="362937263322676",
    api_secret="w339Gv4z_NcM7gvOPmiq5QloAB0"
)

