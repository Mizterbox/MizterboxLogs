from flask import Flask, request, jsonify
from datetime import datetime
import pytz
from pytz import timezone
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://dbezkeuzwkxhnk:f0a41da23f5932a1f4a891b5e3b57c20b36f3b236614b74a8aa2e95e22f7c4d9@ec2-54-221-253-228.compute-1.amazonaws.com:5432/d686176j9ebd4h'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://logs:mizterbox@localhost:5432/mizterboxlogs'
db = SQLAlchemy(app)



from app_local.models import MizterboxLogs
from app_local import routes
