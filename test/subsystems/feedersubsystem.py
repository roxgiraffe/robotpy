#Hhhhhhh
from commands2 import SubsystemBase
from ctre import WPI_VictorSPX


class FeederSubsystem(SubsystemBase):
    def __init__(self):
        super().__init__()
        self.mg = WPI_VictorSPX(9)