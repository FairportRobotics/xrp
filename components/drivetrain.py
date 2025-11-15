from magicbot import feedback
import wpilib.drive
import xrp


class Drivetrain:
    left_motor: xrp.XRPMotor
    right_motor: xrp.XRPMotor

    mode: str = "arcade"  # Default mode

    def setup(self):
        self.drive = wpilib.drive.DifferentialDrive(self.left_motor, self.right_motor)

    def execute(self):
        pass

    def go(self, left_stick: float, right_stick: float):
        """Make the robot drive based on the current mode."""
        if self.mode == "tank":
            self.drive.tankDrive(left_stick, right_stick)
        elif self.mode == "curvature":
            self.drive.curvatureDrive(left_stick, right_stick, allowTurnInPlace=True)
        else:
            self.drive.arcadeDrive(left_stick, right_stick, squareInputs=True)

    def stop(self):
        """Stop the drivetrain motors."""
        self.drive.stopMotor()

    @feedback(key="Mode")
    def get_mode(self) -> str:
        """Get the current drive mode."""
        return self.mode

    def set_mode(self, mode: str):
        """
        Set the drive mode.

        :param mode: The drive mode to set, either "arcade", "curvature" or "tank".
        """
        if mode not in ("arcade", "curvature", "tank"):
            raise ValueError("Invalid drive mode. Use 'arcade', 'curvature' or 'tank'.")
        self.mode = mode
