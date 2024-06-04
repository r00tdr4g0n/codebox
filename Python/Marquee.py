import threading
import time

__isWorking: bool = True

def Marquee(a_str: str):
    global __isWorking
    
    __isWorking = True
    
    ch: list = ['\\', '|', '/', '-']
    idx: int = 0
    
    while __isWorking:
        print(f"{a_str} {ch[idx]}", end='\r')
        idx += 1
        idx %= len(ch)
        time.sleep(0.1)
        
def MarqueeTest():
    global __isWorking
    
    marqueeThread = threading.Thread(target=Marquee, args=("Connecting...", ))
    marqueeThread.start()
    time.sleep(3)
    __isWorking = False
    
    if marqueeThread is not None:
        while marqueeThread.is_alive():
            pass
    
