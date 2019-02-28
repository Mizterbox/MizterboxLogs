from datetime import datetime
from app_local import db
from app_local.utilities import capture_timestamp

class MizterboxLogs(db.Model):
    """
    Logs for sprinklers.
    """

    id = db.Column(db.Integer,primary_key=True)
    sprinklerid = db.Column(db.Integer,nullable=False)
    status = db.Column(db.String(30),nullable=False)
    timestamp = db.Column(db.DateTime,nullable=False,default=capture_timestamp())

    def __repr__(self):
        return f"MizterboxLogs('{self.id}','{self.sprinklerid}','{self.status}','{self.timestamp}')"


class Sprinker(db.Model):
    """
    Generate a sprinkler id from a setup.
    """
    id = db.Column(db.Integer,primary_key=True)
    sprinklerid = db.Column(db.Integer,nullable=False)
    address = db.Column(db.String(80),nullable=False)
    timestamp = db.Column(db.DateTime,nullable=False,default=capture_timestamp())

    def __repr__(self):
        return f"Sprinkler('{self.id}','{self.sprinklerid}','{self.address}','{self.timestamp}')"
