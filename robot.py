import components
import constants
import magicbot
import os
import wpilib
import xrp

os.environ["HALSIMXRP_HOST"] = "192.168.42.1"
os.environ["HALSIMXRP_PORT"] = "3540"


class Robot(magicbot.MagicRobot):
    accelerometer: components.Accelerometer
    controller: components.XboxController
    distance_sensor = components.DistanceSensor
    drivetrain: components.DriveTrain
    gyro: components.Gyro
    led: components.LED
    reflectance_sensor: components.ReflectanceSensor

    def createObjects(self):
        # Controller stuff here
        self.controller_correct_for_deadband = True
        self.controller_deadband = constants.CONTROLLER_DEADBAND
        self.controller_port = constants.CONTROLLER_PORT

        # Drivetrain stuff here
        self.drivetrain_left_motor = xrp.XRPMotor(constants.LEFT_MOTOR_DEVICE_NUMBER)
        self.drivetrain_left_encoder = wpilib.Encoder(
            constants.LEFT_ENCODER_CHANNEL[0], constants.LEFT_ENCODER_CHANNEL[1]
        )
        self.drivetrain_right_motor = xrp.XRPMotor(constants.RIGHT_MOTOR_DEVICE_NUMBER)
        self.drivetrain_right_encoder = wpilib.Encoder(
            constants.RIGHT_ENCODER_CHANNEL[0], constants.RIGHT_ENCODER_CHANNEL[1]
        )
        self.drivetrain_encoder_units = constants.ENCODER_UNITS

        # Gyro - Passed into the gyro and accelerometer components
        self.xrp_gyro = xrp.XRPGyro()

    def teleopPeriodic(self):
        self.controller.capture_buton_presses()

        left_x, left_y, right_x, right_y = self.controller.get_joysticks()
        if self.drivetrain.get_mode() == "tank":
            self.drivetrain.go(-left_y, -right_y)
        else:
            self.drivetrain.go(-left_y, -right_x)
