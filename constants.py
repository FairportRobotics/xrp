import math

# ============================================================
# CONTROLLER CONSTANTS
# ============================================================
# The port the controller is connected to
CONTROLLER_PORT = 0

# ============================================================
# MOTOR CONSTANTS
# ============================================================
# The XRP has the left and right motors set to
# PWM channels 0 and 1 respectively
LEFT_MOTOR_CHANNEL = 0
RIGHT_MOTOR_CHANNEL = 1

# The XRP has onboard encoders that are hardcoded
# to use DIO pins 4/5 and 6/7 for the left and right
LEFT_ENCODER_A_CHANNEL = 4
LEFT_ENCODER_B_CHANNEL = 5
RIGHT_ENCODER_A_CHANNEL = 6
RIGHT_ENCODER_B_CHANNEL = 7

# Based on the datasheet, the wheel diameter is 60mm. Converting the diameter to inches
WHEEL_DIAMETER_INCH = 60 / 25.4

# The encoder has this many ticks per revolution of the motor shaft
# (NOT the wheel itself)
ENCODER_RESOLUTION = 12  # From datasheet

# The gear ratio is how many times the motor shaft has to spin
# for the wheels to make one full rotation
MOTOR_GEAR_RATIO = 48.75  # From datasheet

# We can tell the encoder to use distance per pulse
# This changes the values returned by getDistance() to be in inches
DISTANCE_PER_PULSE = (WHEEL_DIAMETER_INCH * math.pi) / (
    ENCODER_RESOLUTION * MOTOR_GEAR_RATIO
)
