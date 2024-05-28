from datetime import datetime

def GetCurrentTime() -> dict:
    currTime: datetime = datetime.now()
    currTimeInfo: dict = {
        "year": currTime.year,
        "mon": currTime.month,
        "day": currTime.day,
        "hour": currTime.hour,
        "min": currTime.min,
        "sec": currTime.second,
        "msec": currTime.microsecond,
        "strDate": currTime.strftime('%y-%m-%d %H:%M:%S.%f')
    }
    
    return currTimeInfo