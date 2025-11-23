import magicbot
import wpilib
import xrp

class IndividualMotor:
    channel: int
    encoder_channel_a: int
    encoder_channel_b: int

    def execute(self):
        pass

    def setup(self):
        self.motor_speed 0.0
        self.motor_encoder_count = 0
        self.motor = xrp.XRPMotor(self.channel)
        self.encoder = wpilib.Encoder(self.encoder_channel_a, self.encoder_channel_b)

    # =========================================================================
    # CONTROL METHODS
    # =========================================================================

    def set_inverted(self):
        """Invert the motor"""
        self.motor.setInverted(True)

    def set_speed(self, rpm):
        """Set the Speed (rpm)"""
        self.motor_speed = rpm

    # =========================================================================
    # INFORMATIONAL METHODS
    # =========================================================================

    @magicbot.feedback(key="encoder count")
    def encoder_count(self) -> int:
        return self.encoder.getDistance()
    
    @magicbot.feedback(key="speed")
    def speed(self) -> float:
        return self.encoder.getRate()

    