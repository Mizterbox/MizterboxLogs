from flask import Flask, request, jsonify
from datetime import datetime
import pytz
from pytz import timezone

app = Flask(__name__)

@app.route("/")
def hello():
    return "Listening to Mizterbox Logs!"


@app.route("/sprinklerlogs/",methods=['GET','POST'])
def sprinklerlogs():
    # register the time as soon as the route was hit
    date_format='%m/%d/%Y %H:%M:%S %Z'
    date = datetime.now(tz=pytz.utc)
    date = date.astimezone(timezone('US/Pacific'))

    content = request.get_json()
    sprinklerid = content['id']
    status = content['status']

    return jsonify(sprinklerid=sprinklerid,
    status=status,
    timestamp=date)


if __name__ == '__main__':
   app.run()
