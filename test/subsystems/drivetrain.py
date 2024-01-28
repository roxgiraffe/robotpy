from commands2 import SubsystemBase
import wpilib
import wpilib.drive
#It imports everything from the libraries

from ctre import WPI_TalonFX, WPI_TalonSRX

class DrivetrainSubsystem(SubsystemBase):#basically just makes different "SubSystems"
    def __init__(self):
        super().__init__()
        mgl = wpilib.SpeedControllerGroup(WPI_TalonSRX(0), WPI_TalonFX(1))#Groups both motors from one side, left in this case
        mgr = wpilib.MotorControllerGroup(WPI_TalonSRX(6), WPI_TalonFX(2))#Groups both motors on the right side
        mgl.setInverted(True)#Motors are inverted because of the way the motors were placed on the robot
        self.dd = wpilib.drive.DifferentialDrive(mgl, mgr)#links it to the differential drive
        self.dd.setSafetyEnabled(False)