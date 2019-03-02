from flask import Flask, request, jsonify
from datetime import datetime
import pytz
from pytz import timezone
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/postgresql-infinite-38158'
db = SQLAlchemy(app)



from app_local.models import MizterboxLogs
from app_local import routes
