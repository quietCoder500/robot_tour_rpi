from controler import *

probe_distance = 10 # distance of probe from center in mm

######################
###  Begin Course  ###
######################
Init(goal_time=45) # 45 seconds to complete the course
Forward(distance=25)
FrontAlign()
Right()
Forward()
Left()
Forward()
Forward()
YawAlign()
Left()
Forward(distance=35)
Backward(distance=35)
Right()
Forward()
Forward()
Forward()
Right()
Forward()
Forward()
YawAlign()
Right()
Forward()
Left()
Forward()
Left()
Forward(distance=35)
Backward(distance=35)
Left()
Forward()
Left()
Forward()
Forward()
Left()
Forward()
Left()
Forward(distance=35)
Backward(distance=35)
Left()
Forward()
Right()
Forward()
Forward()
Left()
Forward()
Forward()
Right()
Forward(probe_distance+50)