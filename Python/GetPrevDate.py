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

def GetPrevDate(a_date: datetime = None) -> dict:
    prevDate: dict = {}
    
    if a_date is None:
        monWith31Days: list = [1, 3, 5, 7, 8, 10, 12]
        monWith30Days: list = [4, 6, 9, 11]

        currDate: datetime = datetime.now()
        currYear: int = currDate.year
        currMon: int = currDate.month
        currDay: int = currDate.day

        if currDay == 1:
            currMon -= 1

            if currMon == 0:
                currMon == 12
                currYear -= 1

            if currMon in monWith30Days:
                currDay = 30
            elif currMon in monWith31Days:
                currDay = 31
            elif currMon == 2:
                if CheckLeap(currYear):
                    currDay = 29
                else:
                    currDay = 28
        else:
            currDay -= 1
        
        prevDate = {
            "year":currYear,
            "mon":currMon,
            "day":currDay,
            "strDate":f"{currYear}{currMon:02d}{currDay:02d}"
        }
    else:
        prevDate = {
            "year":a_date.year,
            "mon":a_date.month,
            "day":a_date.day,
            "strDate":a_date.strftime('%Y%m%d')
        }
    
    return prevDate