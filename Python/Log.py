class Logger:
    def __init__(self, logFileName):
        print(f"{self.__class__.__name__}::__init__")

        self.logFileName = logFileName

        if not os.path.exists("log"):
            os.mkdir("log")

        with open(f"log{os.sep}{self.logFileName}", "a") as lf:
            pass

    def Logging(self, log: str):
        curr = datetime.datetime.now()
        log = f"[{curr.year}-{curr.month:02d}-{curr.day:02d} {curr.hour:02d}:{curr.minute:02d}:{curr.second:02d}.{curr.microsecond // 1000:03d}]\t{log}\n"
        with open(f"log{os.sep}{self.logFileName}", "a") as lf:
            lf.write(log)

    def __del__(self):
        print(f"{self.__class__.__name__}::__del__")
