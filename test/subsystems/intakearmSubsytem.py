from commands2 import Subsystem, SubsystemBase
from ctre import TalonFX, WPI_TalonFX, WPI_VictorSPX
from wpilib import MotorControllerGroup

class IntakeArmSubsystem(SubsystemBase):
    def __init__(self):
         super().__init__() 
         self.mg = WPI_TalonFX(4) #the motor being used for this motor