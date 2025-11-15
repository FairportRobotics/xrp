import xrp


class LED:
    on_board_led: xrp.XRPOnBoardIO

    def execute(self) -> None:
        pass

    def setup(self) -> None:
        """Setup the LED component"""
        # Turn off the LED at the start
        self.off()

    def on(self) -> None:
        """Turn the LED on"""
        self.on_board_led.setLed(True)

    def off(self) -> None:
        """Turn the LED off"""
        self.on_board_led.setLed(False)
