import re
import time
import random
import matplotlib.pyplot as plt
import numpy as np
#from buildhat import MotorPair
probe_distance = 10  # distance of probe from center in mm
average_time = 6  # average time of the robot per function

class PID:
    def __init__(self, Kp, Ki, Kd):
        self.Kp = Kp
        self.Ki = Ki
        self.Kd = Kd
        self.last_error = 0
        self.integral = 0

    def update(self, error, dt):
        derivative = (error - self.last_error) / dt
        self.integral += error * dt
        output = self.Kp * error + self.Ki * self.integral + self.Kd * derivative
        self.last_error = error
        return output
    

class Move():
    def __init__(self, time_target, file_path, motor_a, motor_b):
        with open(file_path, 'r') as f:
            self.file = f.readlines()
        self.time_target = time_target
        self.motor_a = motor_a
        self.motor_b = motor_b
        self.pid = PID(Kp=1.0, Ki=0.1, Kd=0.05)
        #self.pair = MotorPair(motor_a, motor_b)
        

    def run(self):
        self.start_time = time.time()
        #self.pair.set_default_speed(50) # this is the default speed of the robot
        # The Pid controller will determine the speed of the robot based on the time it is taking to complete the tasks
        m.xp = []
        m.yp = []
        i = 0
        adjustment = 1
        last_time_remaining = self.time_target
        while True:
            try:
                line = self.file[i]
            except IndexError:
                break

            # Execute command
             

            time.sleep((60/len(self.file))-(60/len(self.file)*adjustment))



            line = line.strip().removesuffix('\n').lower()
            fchar = line[0]

            time_remaining = self.time_target - (time.time() - self.start_time )
            target = (self.time_target / len(self.file)) * (i + 1)
            error = (self.time_target - target) - time_remaining # error = target - actual
            dt = time_remaining / last_time_remaining
            last_time_remaining = time_remaining
            adjustment = self.pid.update(error, dt)
            self.yp.append(error)
            self.xp.append(time.time() - self.start_time)
            print(f'Error: {error}, Adjustment: {adjustment}')

            




# 1. Initialize the system
m = Move(60, 'sequence.txt', 'C', 'D')

######################
###  Begin Course  ###
######################

# 2. Run the system
m.run()
print(m.xp)
print(m.yp)
xpoints = np.array(m.xp)
ypoints = np.array(m.yp)
plt.plot(xpoints, ypoints)
plt.show()