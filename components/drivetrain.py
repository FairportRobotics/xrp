from magicbot import feedback
import wpilib
import wpilib.drive
import xrp


class Drivetrain:
    left_encoder: wpilib.Encoder
    left_motor: xrp.XRPMotor
    right_encoder: wpilib.Encoder
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

    @feedback(key="Velocity")
    def get_velocity(self) -> float:
        """Returns the average velocity based on the encoders"""
        # Calculate the average speed from both encoders
        speed = (self.left_encoder.getRate() + self.right_encoder.getRate()) / 2.0
        # Return the absolute value rounded to one decimal place
        return round(abs(speed), 1)
