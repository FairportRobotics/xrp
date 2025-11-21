import magicbot
import wpilib
from components.led import LED
from components.xboxcont import XboxController
import xrp 
import os

os.environ["HALSIMXRP_HOST"] = "192.168.42.1"
os.environ["HALSIMXRP_PORT"] = "3540"

class MyRobot(magicbot.MagicRobot):
    led: LED 
    controller: XboxController

    def createObjects(self):
        '''Create motors and stuff here'''
        self.on_board_led = xrp.XRPOnBoardIO()
        self.port = 0

    def teleopInit(self):
        '''Called when teleop starts; optional'''
        self.led.on()

    def teleopPeriodic(self): 
        pass
    
    
    
    
