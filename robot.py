from components.led import LED
from components.controller import XboxController
import magicbot
import os
import wpilib
import xrp

os.environ["HALSIMXRP_HOST"] = "192.168.42.1"
os.environ["HALSIMXRP_PORT"] = "3540"


class MyRobot(magicbot.MagicRobot):
    controller: XboxController
    led: LED

    def createObjects(self):
        """Create motors and stuff here"""
        self.on_board_led = xrp.XRPOnBoardIO()
        self.controller_port = 0

    def teleopInit(self):
        """Called when teleop starts; optional"""
        self.led.on()

    def teleopPeriodic(self):
        pass
