import components
import magicbot
import wpilib.drive


class DriveTrain:
    left_motor: components.IndividualMotor
    right_motor: components.IndividualMotor

    def execute(self):
        pass

    def setup(self):
        self.left_effort = 0.0
        self.right_effort = 0.0
        self.left_speed = 0
        self.right_speed = 0
        self.drive = wpilib.drive.DifferentialDrive(self.left_motor, self.right_motor)

    # =========================================================================
    # CONTROL METHODS
    # =========================================================================

    def reset_encoders(self):
        self.left_motor.encoder.reset()
        self.right_motor.encoder.reset()

    def set_effort(self, left: float, right: float):
        self.left_effort = left
        self.right_effort = right

    def stop_motors(self):
        self.drive.stopMotor()

    def straight(self, cm: float, effort: float = 0.5):
        pass

    def turn(self, degree, effort: float = 0.5):
        pass

    # =========================================================================
    # INFORMATIONAL METHODS
    # =========================================================================

    @magicbot.feedback
    def left_encoder(self) -> float:
        return self.left_motor.encoder.encoder_count()

    @magicbot.feedback
    def right_encoder(self) -> float:
        return self.right_motor.encoder.encoder_count()
