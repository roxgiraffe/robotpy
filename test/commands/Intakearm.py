from commands2 import CommandBase
from wpilib import XboxController

from subsystems.intakearmSubsytem import IntakeArmSubsystem


class IntakeArm(CommandBase): #class
    def __init__(self, s:IntakeArmSubsystem, j:XboxController): #includes subsytems and controller info
        super().__init__()
        self.s = s #variable
        self.j = j #variable
    def execute(self):
        Bu = 1 if self.j.getRawButton(1) is True else 0 #if button 10 is pressed move, else: dont move
        Bd = 1 if self.j.getRawButton(2) is True else 0 #if button 11 is pressed move, else: dont move
        self.s.mg.set((Bu - Bd) * 0.4) #The speed at which the intake arms go at 
        
        