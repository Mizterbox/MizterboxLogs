from app_local import app
from app_local import db
from app_local.utilities import capture_timestamp
from flask import request, jsonify,render_template
from app_local.models import MizterboxLogs


@app.route("/")
def hello():
    return render_template('index.html')


@app.route("/sprinklerlogs/",methods=['GET','POST'])
def sprinklerlogs():
    """
    Listens to JSON Logs from deployed esp8266 systems and stores them into the database.
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


@app.route("/registersprinkler/",methods=['GET','POST'])
def registersprinkler():
    """
    Add a sprinkerler to the database so that the ids can be checked against.
    """
    request.method == 'GET':
        return render_template('registersprinkler.html')


    if request.method == 'POST'
        
