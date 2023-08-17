from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

direito = Motor(Port.B)
garra = Motor(Port.C)
esquerdo = Motor(Port.D, Direction.COUNTERCLOCKWISE)
corD = ColorSensor(Port.E)
corE = ColorSensor(Port.F)

robo = DriveBase(direito, esquerdo, 87.2, 127.4)

hub = PrimeHub()

hub.imu.reset_heading(0)

#Ínicio do código

def SelecionaCor(cor):
    if cor == Color.RED:
        return('R')
    if cor == Color.GREEN:
        return('G')
    if cor == Color.YELLOW:
        return('Y')

def DirCurva(ang):
    if hub.imu.ready() == True:
        
        while hub.imu.heading() < (ang):
            esquerdo.run(100)
            direito.run(-100)
        esquerdo.brake()
        direito.brake()
        hub.imu.reset_heading(0)

def EsqCurva(ang):
    if hub.imu.ready() == True:
        print('oi')
        while hub.imu.heading() > -(ang):
            esquerdo.run(-100)
            direito.run(100)
        esquerdo.brake()
        direito.brake()
        hub.imu.reset_heading(0)

def Andar(cm):
    robo.straight(cm*10)

def Estaciona():
    while corD.reflection() > 6 and corE.reflection() > 6:
        robo.drive(50,0)
    robo.stop()
    if corD.reflection() < 6:
        while corE.reflection() > 6:
            direito.run(90)
        wait(150)
        direito.brake()
    elif corE.reflection() < 6:
        while corD.reflection() > 6:
            esquerdo.run(90)
        wait(150)
        esquerdo.brake()

#Chegada até o ponto central da rampa (comum a todos)

Andar(37.5)
DirCurva(90)
garra.run_time(700000,17000)
Andar(63.5)
Andar(11.5)

cores = [Color.GREEN, Color.RED, Color.YELLOW]

while corD.color() not in cores and corE.color() not in cores:
    robo.drive(95,0)
robo.stop()
cor2 = SelecionaCor(corD.color())
Andar(-5)
DirCurva(90)
while corD.color() not in cores and corE.color() not in cores:
    robo.drive(95,0)
cor3 = SelecionaCor(corD.color())

if cor3 != 'Y' and cor2 != 'Y':
    cor1 = SelecionaCor(Color.YELLOW)
elif cor3 != 'G' and cor2 != 'G':
    cor1 = SelecionaCor(Color.GREEN)
else:
    cor1 = SelecionaCor(Color.RED)
sequencia = f'{cor1}{cor2}{cor3}'
print(sequencia)
DirCurva(90)
Andar(45)
Estaciona()
DirCurva(90)
Andar(11)

garra.run_time(-700000,17000)

if sequencia == 'RGY':
    while corD.color() != Color.RED:
        robo.drive(110, 0)
    robo.stop()
    garra.run_time(900000,16000)
    Andar(-60)
    DirCurva(90)
