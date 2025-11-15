from components.controller import XboxController
from components.drivetrain import Drivetrain
from components.led import LED
import magicbot
import os
import xrp

os.environ["HALSIMXRP_HOST"] = "192.168.42.1"
os.environ["HALSIMXRP_PORT"] = "3540"


class MyRobot(magicbot.MagicRobot):
    # Declare variables and objects here
    controller: XboxController
    drivetrain: Drivetrain
    led: LED

    def createObjects(self):
        """Create motors and stuff here"""
        # Controller stuff here
        self.controller_port = 0
        # Drivetrain stuff here
        self.drivetrain_left_motor = xrp.XRPMotor(0)
        self.drivetrain_right_motor = xrp.XRPMotor(1)
        # LED stuff here
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

        # Do something with the joystick values
        left_x, left_y, right_x, right_y = self.controller.joysticks()
        self.drivetrain.go(-left_y, -right_x)
