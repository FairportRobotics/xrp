import wpilib.drive
import xrp


class Drivetrain:
    left_motor: xrp.XRPMotor
    right_motor: xrp.XRPMotor

    def execute(self) -> None:
        pass

    def setup(self) -> None:
        """Setup the drivetrain"""
        self.drive = wpilib.drive.DifferentialDrive(self.left_motor, self.right_motor)

    def go(self, throttle: float, rotation: float, square_inputs: bool = True) -> None:
        """Drive the robot with the given left and right speeds"""
        self.drive.arcadeDrive(throttle, rotation, squareInputs=square_inputs)

    def stop(self) -> None:
        """Stop the drivetrain"""
        self.drive.stopMotor()
