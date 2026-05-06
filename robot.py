# XRP MagicBot
# To Run: robotpy sim --xrp

from components.xrpled import XRPLed
from components.xrpservo import XRPServo
from components.xrptankdrive import XRPTankDrive
from components.controller import XboxController
import constants
import magicbot
import os

os.environ["HALSIMXRP_HOST"] = "192.168.42.1"
os.environ["HALSIMXRP_PORT"] = "3540"


class MyRobot(magicbot.MagicRobot):
    # Magicbot components
    controller: XboxController
    led: XRPLed
    servo: XRPServo
    tankdrive: XRPTankDrive
    # Robot specific variables
    name: str = constants.Robot.NAME
    servo_change: float = constants.Robot.SERVO_CHANGE

    def createObjects(self):
        self.current_state = "Initializing"
        self.controller_port = constants.Ids.CONTROLLER
        self.servo_channel = constants.Ids.SERVO
        self.led_blink_time = constants.LED_BLINK_TIME

    def autonomousInit(self):
        self.led.mode = "on"

    def disabledInit(self):
        pass

    def disabledPeriodic(self):
        self.led.mode = "off"
        self.tankdrive.stop()

    def teleopInit(self):
        self.led.mode = "blink"

    def teleopPeriodic(self):
        self.current_state = "Running teleop"
        self.tankdrive.drive(-self.controller.left_y, -self.controller.right_x)

        # Servo control with bumpers
        ## Left bumper raises the servo, right bumper lowers it
        if self.controller.left_bumper_pressed():
            self.servo.position += self.servo_change
        elif self.controller.right_bumper_pressed():
            self.servo.position -= self.servo_change

    @magicbot.feedback(key="name")
    def get_name(self) -> str:
        return self.name

    @magicbot.feedback(key="is")
    def get_current_state(self):
        """Return the current state of the robot"""
        return self.current_state
