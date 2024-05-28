from datetime import datetime
import os

__color: dict = {
    "red":31,
    "green":32,
    "yellow":33,
    "blue":34,
    "cyan":36,
    "magenta":35,
}

def ColorPrint(a_str: str = '', a_color: str = None):
    color: int = None
    if a_color in __color:
        color = __color[a_color]
    else:
        color = 0
        
    print(f"\033[{color}m{a_str}\033[0m")

def IsExistDirectory(a_path: str = None) -> bool:
    if (a_path is not None) and (len(a_path) > 0):
        return os.path.isdir(a_path)
    else:
        return False
    
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

def CreateLogFile(a_name) -> bool:
    global __existLogFile
    global __jobName
    global __logFileName 
    
    currTime: dict = GetCurrentTime()
    fileName: str = f"log\\{a_name}_{currTime['year']}{currTime['mon']:02d}{currTime['day']:02d}.log"
    
    if IsExistDirectory('log') == False:
        ColorPrint(f"[{GetCurrentTime()['strDate']}] [fsec] Failed to create log file", "red")
        __existLogFile = False
    else:
        with open(fileName, "a") as f:
            __jobName = a_name
            __logFileName = fileName
    
    return __existLogFile