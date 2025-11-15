from magicbot import AutonomousStateMachine, timed_state
from components.drivetrain import Drivetrain


class DriveForward(AutonomousStateMachine):
<<<<<<< HEAD
=======

>>>>>>> 639ea41d256b709c6d63e39456ada91a29ce34a3
    MODE_NAME = "Drive Forward"
    DEFAULT = True

    # Injected from the definition in robot.py
    drivetrain: Drivetrain

    @timed_state(duration=3, first=True)
    def drive_forward(self):
<<<<<<< HEAD
        self.drivetrain.go(-0.7, 0)
=======
        self.drivetrain.go(-0.7, 0)
>>>>>>> 639ea41d256b709c6d63e39456ada91a29ce34a3
