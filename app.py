from flask import Flask, request, jsonify
from time import gmtime, strftime, localtime
from dateutil import tz

app = Flask(__name__)

@app.route("/")
def hello():
    return "Listening to Mizterbox Logs!"


@app.route("/sprinklerlogs/",methods=['GET','POST'])
def sprinklerlogs():

    content = request.get_json()
    sprinklerid = content['id']
    status = content['status']
    from_zone = tz.getutil('UTC')
    to_zone = tz.gettz('America/Los_Angeles')

    utc_timestamp = strftime("%Y-%m-%d %H:%M:%S", localtime())

    # Tell the datetime object that it's in UTC time zone since
    # datetime objects are 'naive' by default
    utc_timestamp = utc.replace(tzinfo=from_zone)

    # Convert time zone
    pacific_ts = utc.astimezone(to_zone)
    return jsonify(sprinklerid=sprinklerid,
    status=status,
    timestamp = pacific_ts)


if __name__ == '__main__':
   app.run()
