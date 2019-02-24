from flask import Flask, request, jsonify
from time import gmtime, strftime, localtime


app = Flask(__name__)

@app.route("/")
def hello():
    return "Listening to Mizterbox Logs!"


@app.route("/sprinklerlogs/",methods=['GET','POST'])
def sprinklerlogs():

    content = request.get_json()
    sprinklerid = content['id']
    status = content['status']
    timestamp = strftime("%Y-%m-%d %H:%M:%S", localtime())
    return jsonify(sprinklerid=sprinklerid,
    status=status,
    timestamp = timestamp)


if __name__ == '__main__':
   app.run()
