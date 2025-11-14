import xrp


class LED:
    on_board_led: xrp.XRPOnBoardIO

    def execute(self):
        pass

    def setup(self):
        self.off()

    def off(self):
        self.on_board_led.setLed(False)

    def on(self):
        self.on_board_led.setLed(True)
