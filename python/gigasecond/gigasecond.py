from datetime import datetime, timedelta

def add_gigasecond(moment=None):
    """Calculate the moment when someone has lived for 10^9 seconds."""

    if moment is None:
        moment = datetime.now()

    return moment + timedelta(seconds=10**9)
