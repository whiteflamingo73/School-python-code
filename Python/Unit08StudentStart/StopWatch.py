import time

class StopWatch:
    def __init__(self, startTime=0, endTime=0):
        self.startTime = startTime
        self.endTime = endTime

    def start(self):
        self.startTime = int(time.time() * 1000)/1000
        

    def stop(self):
        self.endTime = time.time()
        
    
    def returnTime(self, thetime= time.time()):
        totalSeconds = int(thetime)
        totalMinutes = totalSeconds // 60
        totalHours = (totalMinutes // 60) - 5
        totalMilliseconds = int(thetime * 1000)

        currentHours = totalHours % 24
        currentMinutes = totalMinutes % 60
        currentSeconds = totalSeconds % 60
        currentMilliseconds = totalMilliseconds % 1000

        #print(f'{currentHours}:{currentMinutes}:{currentSeconds}:{currentMilliseconds}')
        return (f'{currentHours}:{currentMinutes}:{currentSeconds}:{currentMilliseconds}')

    def getStartTime(self):
        return self.returnTime(self.startTime)

    def getEndTime(self):
        return self.returnTime(self.endTime)

    def getElapsed(self):
        
        return self.returnTime(self.endTime - self.startTime)
    
    #def getEnd(self):
    #    self.returnTime(self.endTime)
    
    #def getBeginning(self):
    #    self.returnTime(self.startTime)


        
