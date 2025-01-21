import re
from functools import wraps
import time
probe_distance = 10 # distance of probe from center in mm
ttime = 60 # total time remainting
average_speed = 6 # average speed of the robot per function
class Move():
    def __init__(self, time, file_path, motor_a, motor_b):
        self.time = time
        with open(file_path, 'r') as f:
            self.file = f.readlines()
        self.motor_a = motor_a
        self.motor_b = motor_b

    def time_it(func):
        
        @wraps(func)
        def wrapper(*args,**kwargs):
            global ttime
            start = time.time()
            result = func(*args,**kwargs)
            ttime = (time.time()-start)
            return result
        return wrapper

    def run(self):
        global ttime
        i = 0
        speed = self.time/(len(self.file)+1)
        while True:
            try:
                line = self.file[i]
            except IndexError:
                break
            # time_total - time used/lines_left
            if len(self.file) == 0:
                speed = self.time-ttime
            else:
                speed = self.time-(ttime/(len(self.file)-i+1))
            line = line.strip().removesuffix('\n').lower()
            fchar = line[0]
            if fchar == 'f':
                if line.find("frontalign") != -1:
                    self._front_align(speed=speed)
                elif line.find("(d") != -1:
                    dist = line[line.find("(")+1:line.find(")")]
                    self._forward(distance=dist.removeprefix("distance="), speed=speed)
                elif line.find("(p") != -1:
                    dist = line[line.find("(")+1:line.find(")")]
                    self._forward(distance=dist, speed=speed)
                else:
                    self._forward(speed=speed)
            elif fchar == 'b':
                self._backward(speed=speed)
            elif fchar == 'r':
                self._right(speed=speed)
            elif fchar == 'l':
                self._left(speed=speed)
            elif fchar == 'y':
                self._yaw_align(speed=speed)
            i += 1

    @time_it
    def _forward(self, distance="50", speed=50):
        print('Forward', eval(distance)) # WARN: eval is dangerous (we are going to use it for now)
        time.sleep(average_speed/((speed/100)+1))

    @time_it
    def _backward(self, speed=50):
        print('Backward')
        time.sleep(average_speed/((speed/100)+1))

    @time_it
    def _right(self, speed=50):
        print('Right')
        time.sleep(average_speed/((speed/100)+1))

    @time_it
    def _left(self, speed=50):
        print('Left')
        time.sleep(average_speed/((speed/100)+1))
    
    @time_it
    def _front_align(self, speed=50):
        print('Front Align')
        time.sleep(average_speed/((speed/100)+1))

    @time_it
    def _yaw_align(self, speed=50):
        print('Yaw Align')
        time.sleep(average_speed/((speed/100)+1))


# 1. Initialize the system
m = Move(60, 'sequence.txt', 'C', 'D')

######################
###  Begin Course  ###
######################

# 2. Run the system
m.run()
print(ttime)