import components
import constants
import magicbot
import os
import wpilib
import xrp

os.environ["HALSIMXRP_HOST"] = "192.168.42.1"
os.environ["HALSIMXRP_PORT"] = "3540"


class MyRobot(magicbot.MagicRobot):
    # Declare variables and objects here
    controller: components.XboxController
    drivetrain: components.DriveTrain
    led: component.LED
    left_motor: components.IndividualMotor
    right_motor: components.IndividualMotor

    def createObjects(self):
        """Create motors and stuff here"""
        # Controller stuff here
        self.controller_port = constants.CONTROLLER_PORT
        # Drivetrain stuff here
        self.left_motor_channel = constants.LEFT_MOTOR_CHANNEL
        self.right_motor_channel = constants.RIGHT_MOTOR_CHANNEL
        self.right_motor.set_inverted()

    def teleopInit(self):
        """Called when teleop starts; optional"""
        pass

    def teleopPeriodic(self):
        """Called periodically during teleop"""
        self.led.blink()
        self.controller.capture_buton_presses()

        # Do something with the joystick values
        # Get the input from the controller
        left_x, left_y, right_x, right_y = self.controller.get_joysticks()
        # if self.drivetrain.get_mode() == "tank":
        #    self.drivetrain.go(-left_y, -right_y)
        # else:
        #    self.drivetrain.go(-left_y, -right_x)
