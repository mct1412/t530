#!/usr/bin/python
# -*- coding:utf-8 -*-

import threading
import time
import Queue

exitFlag = 0

class myThread(threading.Thread):
    def __init__(self, thread, Queue):
        threading.Thread.__init__(self)
        self.threadname = thread
        self.q = Queue
    
    def run(self):
        print("start %s: " % self.threadname)
        processData(self.threadname, self.q)
        print("end %s: " % self.threadname)

def processData(threadname, q):
    while not exitFlag:
        threadLock.acquire()
        if not q.empty():
            data = q.get()
            threadLock.release()
            print("%s %s" % (threadname,data))    
        else:
            threadLock.release()
        time.sleep(1)



nameList=["thread01", "thread02", "thread03"]
dataList=["one", "two", "three", "four", "five"]
threadLock=threading.Lock()
queue=Queue.Queue(10)
threads=[]

for i in nameList:
    thread = myThread(i,queue)
    thread.start()
    threads.append(thread)

threadLock.acquire()
for j in dataList:
    queue.put(j) 
threadLock.release()

while not queue.empty():
    pass

exitFlag = 1

for t in threads:
    t.join()

print("All Done.")

