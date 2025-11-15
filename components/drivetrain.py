import wpilib.drive
import xrp


class DriveTrain:
    left_motor: xrp.XRPMotor
    right_motor: xrp.XRPMotor

    def setup(self):
        self.drive = wpilib.drive.DifferentialDrive(self.left_motor, self.right_motor)

    def execute(self):
        pass

    def move(self, left_stick: float, right_stick: float) -> None:
        """Make the robot move."""
        self.drive.arcadeDrive(-left_stick, -right_stick, squareInputs=True)

    def stop(self) -> None:
        """Stop the drivetrain motors."""
        self.drive.stopMotor()