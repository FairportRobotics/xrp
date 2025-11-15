from magicbot import AutonomousStateMachine, timed_state
from components.drivetrain import Drivetrain


class DriveForward(AutonomousStateMachine):
    MODE_NAME = "Drive Forward"
    DEFAULT = True

    # Injected from the definition in robot.py
    drivetrain: Drivetrain

    @timed_state(duration=3, first=True)
    def drive_forward(self):
        self.drivetrain.go(-0.7, 0)
