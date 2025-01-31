import time

class StopWatch:
    def __init__(self):
        self.__startTime = 0
        self.__endTime = 0

    def start(self):
        self.__startTime = time.time()
        return self.__startTime

    def stop(self):
        self.__endTime = time.time()
        return self.__endTime
    
    def returnTime(self, thetime= time.time()):
        totalSeconds = int(thetime)
        totalMinutes = totalSeconds // 60
        totalHours = (totalMinutes // 60) - 5
        totalMilliseconds = int(thetime * 1000)

        currentHours = totalHours % 24
        currentMinutes = totalMinutes % 60
        currentSeconds = totalSeconds % 60
        currentMilliseconds = totalMilliseconds % 100

        print(f'{currentHours}:{currentMinutes}:{currentSeconds}:{currentMilliseconds}')
        return (f'{currentHours}:{currentMinutes}:{currentSeconds}:{currentMilliseconds}')

    def getStartTime(self):
        self.start()
        return self.returnTime(self.__startTime)

    def getEndTime(self):
        self.stop()
        return self.returnTime(self.__endTime)

    def getElapsed(self):
        
        return self.returnTime(self.__endTime - self.__startTime)


        
