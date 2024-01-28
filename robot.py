import wpilib
import commands2
from commands.Intake import Intake
from commands.Intakearm import IntakeArm
from commands.climb import Climb
from commands.drive import Drive
from commands.feeder import Feeder
from commands.shooter import Shooter
from subsystems.ShooterSubsystem import ShooterSubsytem
from subsystems.climbingSubsytem import ClimbingarmSubsytem
from subsystems.drivetrain import DrivetrainSubsystem
from subsystems.feedersubsystem import FeederSubsystem
from subsystems.intakearmSubsytem import IntakeArmSubsystem
from subsystems.IntakeSubsystem import IntakeSubsystem

class EpicRobot(commands2.TimedCommandRobot):
    def __init__(self):
        super().__init__()
        self.controller = wpilib.Joystick(port=0)
        self.controller2 = wpilib.XboxController(port=2)
        self.drivejoystick = wpilib.Joystick(0) #Joystick info
        self.drivejoystick2 = wpilib.XboxController(2)
        self.s_drive = DrivetrainSubsystem()
        self.c_drive = Drive(self.s_drive, self.drivejoystick2)#joystick stuff
        self.s_arm = ClimbingarmSubsytem()
        self.c_arm = Climb(self.s_arm, self.drivejoystick2)#joystick stuff
        self.s_intakearm = IntakeArmSubsystem()
        self.c_intakearm = IntakeArm(self.s_intakearm, self.drivejoystick2)#joystick stuff
        self.s_intake = IntakeSubsystem()
        self.c_intake = Intake(self.s_intake, self.drivejoystick)
        self.s_feeder = FeederSubsystem()
        self.c_feeder = Feeder(self.s_feeder, self.drivejoystick)
        self.s_shooter = ShooterSubsytem()
        self.c_shooter = Shooter(self.s_shooter, self.drivejoystick)
    def teleopInit(self) -> None:# basically saying that when robot is operated then allow the following to work
        self.c_drive.schedule()
        self.c_arm.schedule()
        self.c_intakearm.schedule()
        self.c_intake.schedule()
        self.c_feeder.schedule()
        self.c_shooter.schedule()
        return super().teleopInit()

if __name__ == '__main__': wpilib.run(EpicRobot)