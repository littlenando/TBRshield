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

robo = DriveBase(esquerdo, direito, 87, 126)
garra = DriveBase(garraA,garraB,19,100)

corD = ColorSensor(Port.E)
corE = ColorSensor(Port.F)


hub.system.set_stop_button((Button.BLUETOOTH))

#Ínicio do código

def EsqCurva(ang):
    if hub.imu.ready() == True:
        print('oi')
        while hub.imu.heading() > -(ang):
            esquerdo.run(100)
            direito.run(-100)
        esquerdo.brake()
        direito.brake()
        hub.imu.reset_heading(0)

def DirCurva(ang):
    if hub.imu.ready() == True:
        print('oi')
        while hub.imu.heading() < (ang):
            esquerdo.run(-100)
            direito.run(100)
        esquerdo.brake()
        direito.brake()
        hub.imu.reset_heading(0)

def Estaciona(cor):
    while corD.color() != cor and corE.color() != cor:
        robo.drive(50,0)
        print (corD.color())
    robo.stop()
    if corD.color() == cor:
        while corE.color() != cor:
            direito.run(90)
        wait(150)
        direito.brake()
    elif corE.color() == cor:
        while corD.color() != cor:
            esquerdo.run(90)
        wait(150)
        esquerdo.brake()

Estaciona(Color.NONE)
robo.straight(-50)
Estaciona(Color.NONE)
