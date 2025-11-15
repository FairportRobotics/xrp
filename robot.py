import magicbot
import os
import wpilib.drive
import xrp

os.environ["HALSIMXRP_HOST"] = "192.168.42.1"
os.environ["HALSIMXRP_PORT"] = "3540"


class MyRobot(magicbot.MagicRobot):
    CYCLES: int = 0

    def createObjects(self):
        """Create motors and stuff here"""
        self.left_motor = xrp.XRPMotor(0)
        self.right_motor = xrp.XRPMotor(1)
        self.right_motor.setInverted(True)
        self.drive = wpilib.drive.DifferentialDrive(self.left_motor, self.right_motor)

    def teleopInit(self):
        """Called when teleop starts; optional"""

    def teleopPeriodic(self):
        """Called periodically during teleop"""
        self.CYCLES += 1
        self.drive.arcadeDrive(0.5, 0)
