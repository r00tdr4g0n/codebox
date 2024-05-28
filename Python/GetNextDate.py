from datetime import datetime

def CheckLeap(a_year: int) -> bool:
    if a_year % 4 == 0:
        if a_year % 100 == 0:
            if a_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

def GetNextDate(a_date: str) -> str:
    date: datetime = datetime.strptime(a_date, "%Y%m%d")
    dateDict: dict = {
        'year': date.year,
        'mon': date.month,
        'day': date.day,
    }
    
    monWith31Days: list = [1, 3, 5, 7, 8, 10, 12]
    monWith30Days: list = [4, 6, 9, 11]
    
    if (dateDict['day'] == 31 and dateDict['mon'] in monWith31Days) \
    or (dateDict['day'] == 30 and dateDict['mon'] in monWith30Days) \
    or (dateDict['mon'] == 2 and dateDict['day'] == (29 if CheckLeap(dateDict['year']) else 28)):
        dateDict['day'] = 1
        
        if dateDict['mon'] == 12:
            dateDict['mon'] = 1
            dateDict['year'] += 1
        else:
            dateDict['mon'] += 1
    else:
        dateDict['day'] += 1
        
    return f"{dateDict['year']}{dateDict['mon']:02d}{dateDict['day']:02d}"