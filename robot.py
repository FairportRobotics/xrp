from components.drivetrain import DriveTrain
from components.led import LED
import magicbot
import os
import xrp

os.environ["HALSIMXRP_HOST"] = "192.168.42.1"
os.environ["HALSIMXRP_PORT"] = "3540"

class MyRobot(magicbot.MagicRobot):
    drivetrain: DriveTrain
    led: LED

    def createObjects(self):
        '''Create motors and stuff here'''
        # Drivetrain stuff here
        self.drivetrain_left_motor = xrp.XRPMotor(0)
        self.drivetrain_right_motor = xrp.XRPMotor(1)
        self.drivetrain_right_motor.setInverted(True)

    def autonomousInit(self) -> None:
        self.led.blink()
    
    def teleopInit(self) -> None:
        '''Called when teleop starts; optional'''
        self.led.turn_on()

    def teleopPeriodic(self) -> None:
        '''Called periodically during teleop'''
        pass