import re
import time
import random

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
        self.time_target = time_target
        with open(file_path, 'r') as f:
            self.file = f.readlines()
        self.motor_a = motor_a
        self.motor_b = motor_b
        self.pid = PID(Kp=1.0, Ki=0.1, Kd=0.05)
        

    def run(self):
        self.start_time = time.time()
        self.last_time = time.time()
        
        speed = self.time_target / self.file.__len__()
        i = 0

        while True:
            try:
                line = self.file[i]
            except IndexError:
                break

            # Execute command
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

            # Adjust speed using PID controller
            speed = self.time_target-(time.time()-self.start_time) / (self.file.__len__()-i-1)
            elapsed_time = time.time() - self.start_time
            error = self.time_target - elapsed_time
            dt = time.time() - self.last_time
            self.last_time = time.time()
            speed_adjustment = self.pid.update(error, dt)
            speed += speed_adjustment
            print(f"Speed: {speed}")
            print("speed_adjustment: ", speed_adjustment)
            i += 1


    def _forward(self, distance="50", speed=1):
        print('Forward', eval(distance))  # WARN: eval is dangerous (we are going to use it for now)
        time.sleep((average_time/(speed/100)))

    def _backward(self, speed=1):
        print('Backward')
        time.sleep((average_time/(speed/100)))

    def _right(self, speed=1):
        print('Right')
        time.sleep((average_time/(speed/100)))

    def _left(self, speed=1):
        print('Left')
        time.sleep((average_time/(speed/100)))
    
    def _front_align(self, speed=1):
        print('Front Align')
        time.sleep((average_time/(speed/100)))

    def _yaw_align(self, speed=1):
        print('Yaw Align')
        time.sleep((average_time/(speed/100)))


# 1. Initialize the system
m = Move(60, 'sequence.txt', 'C', 'D')

######################
###  Begin Course  ###
######################

# 2. Run the system
m.run()
print(m.time_target-(time.time()-m.start_time))