from components.controller import XboxController
from components.led import LED
import magicbot
import os
import xrp

os.environ["HALSIMXRP_HOST"] = "192.168.42.1"
os.environ["HALSIMXRP_PORT"] = "3540"


class MyRobot(magicbot.MagicRobot):
    # Declare variables and objects here
    controller: XboxController
    led: LED

    def createObjects(self):
        """Create motors and stuff here"""
        self.controller_port = 0
        self.on_board_led = xrp.XRPOnBoardIO()

    def teleopInit(self):
        """Called when teleop starts; optional"""
        # Turn on the LED when teleop starts
        self.led.on()

    def teleopPeriodic(self):
        """Called periodically during teleop"""

        # Turn on the LED if X is pressed, turn it off if Y is pressed
        if self.controller.x_pressed():
            self.led.on()
        elif self.controller.y_pressed():
            self.led.off()
