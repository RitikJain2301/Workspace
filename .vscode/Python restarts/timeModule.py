import time
import datetime

currnt=datetime.datetime.now()
t=time.strftime("%d-%m-%d %H:%M:%S",time.localtime())
print(t)