import random
import time
def randomdatetime(start, end):
    print("Printing date between ", start, " and ", end, "..."  )
    randoms = random.random()
    frmat = '%m/%d/%Y'
    stime = time.mktime(time.strptime(start, frmat))
    etime = time.mktime(time.strptime(end, frmat))
    randTime = stime + randoms*(etime - stime)
    rdate = time.strftime(frmat, time.localtime(randTime))
    return rdate

print("generating random date... \n", randomdatetime("1/1/2026", "1/1/2027"))
    
    
