from commands2 import CommandBase
from wpilib import XboxController
from subsystems.climbingSubsytem import ClimbingarmSubsytem


class Climb(CommandBase):
    def __init__(self, s:ClimbingarmSubsytem, j:XboxController):
        super().__init__()
        self.s = s #variable, replacement name for the ClimbingarmSubsystem
        self.j = j #variable, replacement name fir the joystick class
    def execute(self):
        bu = 1 if self.j.getRawButton(5) is True else 0 #saying if its pressed then move foward if not then for it not to move
        bd = 1 if self.j.getRawButton(6) is True else 0 #if button 7 is pressed move bakwards if not then dont move.
        self.s.mgl.set((bu - bd)* 0.10) #The speed at which the climb arms move at

