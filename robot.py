from components.drivetrain import Drivetrain
from components.led import LED
from components.controller import XboxController
import magicbot
import os
import wpilib
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
        self.drivetrain_right_motor.setInverted(True)

    def teleopInit(self):
        """Called when teleop starts; optional"""
        pass

    def teleopPeriodic(self):
        """Called periodically during teleop"""
        self.led.blink()
        #'''
        # Change the drive mode based on the button pressed
        if self.controller.a_button_pressed():
            self.drivetrain.set_mode("arcade")
        if self.controller.b_button_pressed():
            self.drivetrain.set_mode("tank")
        if self.controller.x_button_pressed():
            self.drivetrain.set_mode("curvature")
        '''
        # self.controller.capture_buton_presses()
        drivetrain_modes = ["arcade", "tank", "curvature"]
        if self.controller.left_bumper_pressed():
            current_mode = self.drivetrain.get_mode()
            next_index = (drivetrain_modes.index(current_mode) + 1) % len(drivetrain_modes)
            self.drivetrain.set_mode(drivetrain_modes[next_index])
        #'''
        # Do something with the joystick values
        # Get the input from the controller
        left_x, left_y, right_x, right_y = self.controller.get_joysticks()
        if self.drivetrain.get_mode() == "tank":
            self.drivetrain.go(-left_y, -right_y)
        else:
            self.drivetrain.go(-left_y, -right_x)
