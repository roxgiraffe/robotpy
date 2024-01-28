from commands2 import CommandBase
from wpilib import Joystick
import wpilib
from subsystems.IntakeSubsystem import IntakeSubsystem


class Intake(CommandBase):
    def __init__(self, s:IntakeSubsystem, j:Joystick):
        super().__init__()
        self.s = s
        self.j = j
    def execute(self):
         b = 1 if self.j.getRawButton(3) is True else 0 
         b2 = 1 if self.j.getRawButton(2) is True else 0 
         self.s.mgl.set((b-b2)*0.5)

         

        
