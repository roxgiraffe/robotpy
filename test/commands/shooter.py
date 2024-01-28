
from commands2 import CommandBase
from wpilib import Joystick
import wpilib
from subsystems.ShooterSubsystem import ShooterSubsytem


class Shooter(CommandBase):
    def __init__(self, s:ShooterSubsytem, j:Joystick):
        super().__init__()
        self.s = s
        self.j = j
    def execute(self):
        b = 1 if self.j.getRawButton(1) is True else 0
        #b2 =  1 if self.j.getRawButton(4) is True else 0
        self.s.m.set(b * 1)
