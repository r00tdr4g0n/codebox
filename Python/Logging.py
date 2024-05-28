from datetime import datetime

__jobName: str = ''
__logFileName: str = ''

__color: dict = {
    "red":31,
    "green":32,
    "yellow":33,
    "blue":34,
    "cyan":36,
    "magenta":35,
}

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

def GetLogFileName() -> str:
    return __logFileName

def ColorPrint(a_str: str = '', a_color: str = None):
    color: int = None
    if a_color in __color:
        color = __color[a_color]
    else:
        color = 0
        
    print(f"\033[{color}m{a_str}\033[0m")

def Logging(a_str: str, a_color: str = None):
    global __existLogFile
    global __jobName
    
    if __existLogFile == True:
        try:
            with open(GetLogFileName(), "a") as f:
                log: str = f"[{GetCurrentTime()['strDate']}] [{__jobName}] {a_str}"
                ColorPrint(log, a_color)
                f.write(log + '\n')
        except Exception as e:
            ColorPrint(f"{e}", "red")