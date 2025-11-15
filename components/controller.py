import wpilib


class XboxController:
    port: int

    def execute(self):
        pass

    def setup(self):
        """Setup the Xbox controller"""
        self.controller = wpilib.XboxController(self.port)

    def joysticks(self) -> tuple[float, float, float, float]:
        """Returns the raw joystick values as a tuple: (left_x, left_y, right_x, right_y)"""
        return (
            self.controller.getLeftX(),
            self.controller.getLeftY(),
            self.controller.getRightX(),
            self.controller.getRightY(),
        )

    def x_pressed(self) -> bool:
        """Returns True if the X button is pressed"""
        return self.controller.getXButton()

    def y_pressed(self) -> bool:
        """Returns True if the X button is pressed"""
        return self.controller.getYButton()
