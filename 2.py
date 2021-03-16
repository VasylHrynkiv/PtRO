import threading
import time
exitFlag = 0

class Thread (threading.Thread):
   def __init__(self, name, counter):
      threading.Thread.__init__(self)
      self.name = name
      self.counter = counter
   def run(self):
      print (self.name + " wakes up...")
      print_time(self.name, self.counter, 3)
      print (self.name + " goes to sleep...")

def print_time(threadName, delay, counter):
   while counter:
      if exitFlag:
         threadName.exit()
      print ("%s: %s" % (threadName, time.ctime(time.time())))
      counter -= 1

worker1 = Thread("Sasha", 1)
worker2 = Thread("Kolya", 2)
worker3 = Thread("Vanya", 3)
worker4 = Thread("Yulya", 4)

worker1.start()
worker2.start()
worker3.start()
worker4.start()

worker1.join()
worker2.join()
worker3.join()
worker4.join()
print ("All work have done!")

#Василь Васильович Гриньків, група КІПЗс-2017
