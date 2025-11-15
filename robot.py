import components
import constants
import magicbot
import os
import xrp

os.environ["HALSIMXRP_HOST"] = "192.168.42.1"
os.environ["HALSIMXRP_PORT"] = "3540"


class MyRobot(magicbot.MagicRobot):
    # Declare variables and objects here
    controller: components.XboxController
    drivetrain: components.Drivetrain
    led: components.LED

    def createObjects(self):
        """Create motors and stuff here"""
        # Controller stuff here
        self.controller_port = constants.CONTROLLER_PORT
        # Drivetrain stuff here
        self.drivetrain_left_motor = xrp.XRPMotor(constants.LEFT_MOTOR_CHANNEL)
        self.drivetrain_right_motor = xrp.XRPMotor(constants.RIGHT_MOTOR_CHANNEL)
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
