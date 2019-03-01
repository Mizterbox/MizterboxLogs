from datetime import datetime
import pytz
from pytz import timezone


def capture_timestamp():
    """
    -------------------------------------
    Captures the current timestamp in PST
    -------------------------------------
    """
    date_format='%Y-%m-%d %H:%M:%S'
    pacific_tz = timezone('US/Pacific')
    timestamp = datetime.now(pacific_tz)
    return timestamp
