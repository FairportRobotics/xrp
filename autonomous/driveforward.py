import components
import magicbot


class DriveForward(magicbot.AutonomousStateMachine):
    # Injected from the definition in robot.py
    drivetrain: components.DriveTrain
    led: components.LED

    MODE_NAME = "Drive Forward"
    DEFAULT = True

    @magicbot.state(first=True, must_finish=True)
    def start(self):
        self.led.turn_on()
        self.next_state("drive_forward")

    @magicbot.timed_state(duration=3, next_state="finish")
    def drive_forward(self):
        # Drive forward at 80% speed
        self.drivetrain.drive.arcadeDrive(0.8, 0.0)

    @magicbot.state()
    def finish(self):
        self.drivetrain.stop()
        self.done()
