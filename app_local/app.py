# from flask import Flask, request, jsonify
# from datetime import datetime
# import pytz
# from pytz import timezone
# from flask_sqlalchemy import SQLAlchemy
#
# def capture_timestamp():
#     """
#     Captures the current timestamp in PST
#     """
#     date_format='%Y-%m-%d %H:%M:%S%z'
#     pacific_tz = timezone('US/Pacific')
#     timestamp = datetime.now(pacific_tz).strftime(date_format)
#     return timestamp
#
#
#
# app = Flask(__name__)
# #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://logs:mizterbox@localhost:3306/mizterboxlogs'
#
#
# @app.route("/")
# def hello():
#     return "Listening to Mizterbox Logs!"
#
#
# @app.route("/sprinklerlogs/",methods=['GET','POST'])
# def sprinklerlogs():
#     # register the time as soon as the route was hit
#     date = capture_timestamp()
#     content = request.get_json()
#     sprinklerid = content['id']
#     status = content['status']
#
#     return jsonify(sprinklerid=sprinklerid,
#     status=status,
#     timestamp=date)
#
#
# if __name__ == '__main__':
#    app.run()
