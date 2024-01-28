
from commands2 import SubsystemBase
from ctre import WPI_TalonFX
from wpilib import MotorControllerGroup


class ClimbingarmSubsytem(SubsystemBase):
    def __init__(self):
         super().__init__()
         mi = WPI_TalonFX(6) #motor
         mi.setInverted(True)
         self.mgl = MotorControllerGroup( mi, WPI_TalonFX(8))#motor group, moves at the same time
