"""my_controller controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = 320
flag=0

leg1=robot.getDevice("front_left")
leg2=robot.getDevice("front_right")
leg3=robot.getDevice("back_left")
leg4=robot.getDevice("back_right")


while robot.step(timestep) != -1:
    if(flag%10==0):
        leg1.setPosition(-0.6)
    elif(flag%10==0.5):
        leg2.setPosition(-0.6)
    elif(flag%10==1):
        leg3.setPosition(-2)     
    elif(flag%10==1.5):
        leg4.setPosition(-2)
        
    elif(flag%10==4):
        # leg1.setPosition(0.4)
        # leg2.setPosition(0.4)
        leg3.setPosition(2)
        leg4.setPosition(2)
    
    flag=flag+1
    



