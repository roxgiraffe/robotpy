from commands2 import SubsystemBase
from ctre import WPI_TalonFX
from wpilib import MotorControllerGroup


class ShooterSubsytem(SubsystemBase):
    def __init__(self):
        super().__init__()
        self.m = WPI_TalonFX(7)
        


