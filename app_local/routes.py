from app_local import app
from app_local import db
from app_local.utilities import capture_timestamp
from flask import request, jsonify,render_template
from app_local.models import MizterboxLogs
from datetime import datetime
from datetime import timedelta
import time


# time difference between now and the last log - in other words:
# the maximum permissible time between now and registered device's last log
# after which one can conclude the registered device under consideration is
# down
PERMITTED_TIME_BETWEEN_CHECKS = timedelta(seconds=45)

@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/sprinklerlogs/",methods=['GET','POST'])
def sprinklerlogs():
    """
    -------------------------------------------------------------------------------------
    Listens to JSON Logs from deployed esp8266 systems and stores them into the database.
    -------------------------------------------------------------------------------------
    """
    # register the time as soon as the route was hit
    date = capture_timestamp()
    content = request.get_json()
    sprinklerid = content['id']
    status = content['status']

    # ORMize the log
    try:
        log = MizterboxLogs(sprinklerid=sprinklerid,status=status,timestamp=date)
        db.session.add(log)
        db.session.commit()
    except:
        raise
    finally:
        db.session.close()

    return jsonify(sprinklerid=sprinklerid,
    status=status,
    timestamp=date)

@app.route("/checkdowns/",methods=['GET'])
def checkdowns():
    """
    ----------------------------------------------------------------------
    Checks to see if any esp8266 devices are down.

    Strategy: Check every registered device and see if time difference between now
    and last log exceeds PERMITTED_TIME_BETWEEN_CHECKS.
    ----------------------------------------------------------------------
    """

    registered_devices = [1,2,4,0]
    down_ids = []

    # this defines the new log windows as time uopdates
    while True:
        # from now, pull up all the records in the last hour.
        last_hour_records = MizterboxLogs.query.filter(MizterboxLogs.timestamp>datetime.now()-timedelta(hours=0,minutes=60))

        # iterate through the available registered devices.
        for registered_device in registered_devices:

            # get the most recent log of the registered_device -> latest log is obtained by picking the last element of the list.
            latest_log = list(MizterboxLogs.query.filter(MizterboxLogs.sprinklerid==registered_device))[-1]

            # if the time difference b/w now and the latest timestamp of the log exceeds 45 minutes (PERMITTED_TIME_BETWEEN_CHECKS)
            # then the system-esp8266 is down.
            current_time = datetime.now()
            if current_time - latest_log.timestamp > PERMITTED_TIME_BETWEEN_CHECKS:
                # add only if the esp8266 isn't present
                if registered_device not in down_ids:
                    down_ids.append(registered_device)

            # if the esp8266 came back up then remove the registered_device from the down list.
            if registered_device in down_ids:
                if current_time - latest_log.timestamp < PERMITTED_TIME_BETWEEN_CHECKS:
                    down_ids.remove(registered_device)

            # delay for sometime
            time.sleep(2)
            print(down_ids)
