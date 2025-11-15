from components.led import LED
import magicbot
import os
import wpilib
import xrp

os.environ["HALSIMXRP_HOST"] = "192.168.42.1"
os.environ["HALSIMXRP_PORT"] = "3540"


class MyRobot(magicbot.MagicRobot):
    # Declare variables and objects here
    led: LED

    def createObjects(self):
        """Create motors and stuff here"""
        self.on_board_led = xrp.XRPOnBoardIO()

    def teleopInit(self):
        """Called when teleop starts; optional"""
        # Turn on the LED when teleop starts
        self.led.on()

    def teleopPeriodic(self):
        pass
