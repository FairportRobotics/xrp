import components
import constants
import magicbot
import math
import wpilib
import wpilib.drive
import wpimath.geometry
import wpimath.kinematics
import xrp


class DriveTrain:
    accelerometer: components.Accelerometer
    encoder_units: str
    gyro: components.Gyro
    left_motor: xrp.XRPMotor
    left_encoder: wpilib.Encoder
    mode: str = "arcade"  # Default mode
    right_motor: xrp.XRPMotor
    right_encoder: wpilib.Encoder

    def execute(self) -> None:
        pass

    def setup(self) -> None:
        self.set_encoder_units(self.encoder_units)
        self.right_motor.setInverted(True)
        self.drive = wpilib.drive.DifferentialDrive(self.left_motor, self.right_motor)
        self.odometry = wpimath.kinematics.DifferentialDriveOdometry(
            wpimath.geometry.Rotation2d.fromDegrees(self.gyro.yaw()),
            self.left_encoder_distance(),
            self.right_encoder_distance(),
            wpimath.geometry.Pose2d(),
        )

    # =========================================================================
    # CONTROL METHODS
    # =========================================================================

    def go(self, left_stick: float, right_stick: float) -> None:
        """Make the robot drive based on the current mode."""
        if self.mode == "tank":
            self.drive.tankDrive(left_stick, right_stick)
        elif self.mode == "curvature":
            self.drive.curvatureDrive(left_stick, right_stick, allowTurnInPlace=True)
        else:
            self.drive.arcadeDrive(left_stick, right_stick, squareInputs=True)

    def reset_encoders(self) -> None:
        self.left_encoder.reset()
        self.right_encoder.reset()

    def reset_gyro(self) -> None:
        self.gyro.reset()

    def reset_odometry(self, pose: wpimath.geometry.Pose2d) -> None:
        self.reset_encoders()
        self.reset_gyro()
        self.odometry.resetPosition(
            wpimath.geometry.Rotation2d.fromDegrees(self.gyro.yaw()),
            self.left_encoder_distance(),
            self.right_encoder_distance(),
            pose,
        )

    def set_encoder_units(self, unit: str) -> None:
        self.encoder_units = unit
        distance_per_pulse = (
            math.pi * constants.WHEEL_DIAMETER[unit]
        ) / constants.COUNTS_PER_REVOLUTION
        self.left_encoder.setDistancePerPulse(distance_per_pulse)
        self.right_encoder.setDistancePerPulse(distance_per_pulse)

    def set_mode(self, mode: str) -> None:
        """
        Set the drive mode.

        :param mode: The drive mode to set, either "arcade", "curvature" or "tank".
        """
        if mode not in ("arcade", "curvature", "tank"):
            raise ValueError("Invalid drive mode. Use 'arcade', 'curvature' or 'tank'.")
        self.mode = mode

    def stop(self) -> None:
        self.drive.stopMotor()    

    # =========================================================================
    # INFORMATIONAL METHODS
    # =========================================================================

    @magicbot.feedback(key="Distance")
    def distance(self) -> float:
        return (self.left_encoder_distance() + self.right_encoder_distance()) / 2.0

    @magicbot.feedback(key="Mode")
    def get_mode(self) -> str:
        return self.mode

    @magicbot.feedback(key="Left Encoder Count")
    def left_encoder_count(self) -> int:
        return self.left_encoder.get()

    @magicbot.feedback(key="Left Encoder Distance")
    def left_encoder_distance(self) -> float:
        return self.left_encoder.getDistance()

    @magicbot.feedback(key="Right Encoder Count")
    def right_encoder_count(self) -> int:
        return self.right_encoder.get()

    @magicbot.feedback(key="Right Encoder Distance")
    def right_encoder_distance(self) -> float:
        return self.right_encoder.getDistance()
