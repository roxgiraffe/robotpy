import commands2
from wpilib import XboxController
from subsystems.drivetrain import DrivetrainSubsystem 

class Drive(commands2.CommandBase):#Creates a class
    def __init__ (self, s:DrivetrainSubsystem, c:XboxController): #Basically brings in the DrivetrainSubsytem class and the xbox class.
        super().__init__()
        self.Subsystem = s #Variable which equals to the Subsystem
        self.joystick = c #Variable for the Joystick
    def initialize(self) -> None:
        return super().initialize()
    def execute(self) -> None:
        jx = self.joystick.getRawAxis(0) * -1 # gets the X-axis, foward/backwards
        jy = self.joystick.getRawAxis(1) # Gets the Y-axis, Turns left/right
        self.Subsystem.dd.arcadeDrive(jy * 0.250, jx * 0.250, False) #Speed the motors are going at/ making it an arcade drive
        return super().execute()