from commands2 import SubsystemBase
from ctre import WPI_VictorSPX
from wpilib import MotorControllerGroup


class IntakeSubsystem(SubsystemBase):
    def __init__ (self):
         super().__init__()
         mi = WPI_VictorSPX(5)
         mi.setInverted(True)
         self.mgl = mi
         