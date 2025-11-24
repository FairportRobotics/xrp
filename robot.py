import components
import constants
import magicbot
import os
import wpilib
import xrp

os.environ["HALSIMXRP_HOST"] = "192.168.42.1"
os.environ["HALSIMXRP_PORT"] = "3540"


class MyRobot(magicbot.MagicRobot):
    # Declare variables and objects here
    accelerometer: components.Accelerometer
    controller: components.XboxController
    distance_sensor = components.Distance
    drivetrain: components.DriveTrain
    gyro: components.Gyro
    led: components.LED
    servo: components.Servo

    def createObjects(self):
        """Create motors and stuff here"""
        # Controller stuff here
        self.controller_port = constants.CONTROLLER_PORT
        # Drivetrain stuff here
        self.drivetrain_left_motor = xrp.XRPMotor(constants.LEFT_MOTOR_CHANNEL)
        self.drivetrain_left_motor_encoder = wpilib.Encoder(
            constants.LEFT_ENCODER_CHANNEL_A, constants.LEFT_ENCODER_CHANNEL_B
        )
        self.drivetrain_right_motor = xrp.XRPMotor(constants.RIGHT_MOTOR_CHANNEL)
        self.drivetrain_right_motor_encoder = wpilib.Encoder(
            constants.RIGHT_ENCODER_CHANNEL_A, constants.RIGHT_ENCODER_CHANNEL_B
        )
        # Servo
        self.servo_channel = constants.SERVO_CHANNEL

    def teleopInit(self):
        """Called when teleop starts; optional"""
        pass

    def teleopPeriodic(self):
        """Called periodically during teleop"""
        self.led.blink()
        self.controller.capture_buton_presses()

        # Do something with the joystick values
        # Get the input from the controller
        left_x, left_y, right_x, right_y = self.controller.get_joysticks()
        # if self.drivetrain.get_mode() == "tank":
        #    self.drivetrain.go(-left_y, -right_y)
        # else:
        #    self.drivetrain.go(-left_y, -right_x)
