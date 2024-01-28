#hhhhhh

from commands2 import CommandBase
from wpilib import Joystick, XboxController

from subsystems.feedersubsystem import FeederSubsystem


class Feeder(CommandBase):
    def __init__(self, s:FeederSubsystem, j:Joystick):
        super().__init__()
        self.s = s
        self.j = j
    def execute(self):
        b1 = 1 if self.j.getRawButton(5) is True else 0
        b2 = 1 if self.j.getRawButton(4) is True else 0
        self.s.mg.set((b1 - b2)*0.5)
