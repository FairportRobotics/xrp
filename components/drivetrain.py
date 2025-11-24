import components
import magicbot
import wpilib
import wpilib.drive
import xrp


class DriveTrain:
    left_motor: xrp.XRPMotor
    left_motor_encoder: wpilib.Encoder
    right_motor: xrp.XRPMotor
    right_motor_encoder: wpilib.Encoder

    def execute(self):
        pass

    def setup(self):
        self.left_effort = 0.0
        self.right_effort = 0.0
        self.left_speed = 0
        self.right_speed = 0
        self.right_motor.setInverted(True)
        self.drive = wpilib.drive.DifferentialDrive(self.left_motor, self.right_motor)

    # =========================================================================
    # CONTROL METHODS
    # =========================================================================

    def reset_encoders(self):
        self.left_motor_encoder.reset()
        self.right_motor_encoder.reset()

    def set_effort(self, left: float, right: float):
        self.left_effort = left
        self.right_effort = right

    def stop_motors(self):
        self.drive.stopMotor()

    def straight(self, distance: float, unit: str = "cm", effort: float = 0.5):
        pass

    def turn(self, degree, effort: float = 0.5):
        pass

    # =========================================================================
    # INFORMATIONAL METHODS
    # =========================================================================

    @magicbot.feedback(key="Left Encoder")
    def left_encoder(self) -> float:
        return self.left_motor_encoder.getDistance()

    @magicbot.feedback(key="Right Encoder")
    def right_encoder(self) -> float:
        return self.right_motor_encoder.getDistance()
