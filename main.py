from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

#Declaração dos objetos
hub = PrimeHub()
esquerdo = Motor(Port.A)
direito = Motor(Port.B, Direction.COUNTERCLOCKWISE)
garraA = Motor(Port.C, Direction.COUNTERCLOCKWISE)
garraB = Motor(Port.D)

movimento = DriveBase(esquerdo, direito, 87, 126)
garra = DriveBase(garraA,garraB,100,100)

corD = ColorSensor(Port.E)
corE = ColorSensor(Port.F)

#Ínicio do código
