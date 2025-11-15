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
        left_motor = xrp.XRPMotor(0)
        right_motor = xrp.XRPMotor(1)
        #right_motor.setInverted(True)
        self.drive = wpilib.drive.DifferentialDrive(left_motor, right_motor)

    def teleopInit(self):
        """Called when teleop starts; optional"""
        pass

    def teleopPeriodic(self):
        """Called periodically during teleop"""
        self.CYCLES += 1
        self.drive.arcadeDrive(0.5, 0)

    @magicbot.feedback
    def get_cycles(self) -> int:
        return self.CYCLES
