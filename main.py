from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

#Declaração dos objetos
hub = PrimeHub()
direito = Motor(Port.D, Direction.COUNTERCLOCKWISE)
esquerdo = Motor(Port.B)
garra = Motor(Port.A)

robo = DriveBase(esquerdo, direito, 87, 126)
robo.settings(200, 1000, 180, 900)

corD = ColorSensor(Port.E)
corE = ColorSensor(Port.F)

garra.run_time(250,1500)


hub.system.set_stop_button((Button.BLUETOOTH))

#Ínicio do código

def SelecionaCor(cor):
    if cor == Color.RED:
        return('R')
    if cor == Color.GREEN:
        return('G')
    if cor == Color.YELLOW:
        return('Y')

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

def Andar(cm):
    robo.straight(cm*10)

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

#Chegada até o ponto central da rampa (comum a todos)
Andar(40.4)
DirCurva(90)
Andar(30)
robo.settings(280, 1000, 180, 900)
Andar(33.5)
robo.settings(180, 1000, 180, 900)
Andar(8)
cor2 = SelecionaCor(corD.color())
Andar(-4)
DirCurva(90)
Andar(3.15)
cor3 = SelecionaCor(corD.color())
print(cor2)

if cor3 != 'Y' and cor2 != 'Y':
    cor1 = SelecionaCor(Color.YELLOW)
elif cor3 != 'G' and cor2 != 'G':
    cor1 = SelecionaCor(Color.GREEN)
else:
    cor1 = SelecionaCor(Color.RED)
sequencia = f'{cor1}{cor2}{cor3}'
print(sequencia)

if sequencia == 'YRG':
    Andar(26.1)
    EsqCurva(90)
    Andar(15.2)
    hub.speaker.beep() #Aqui ele deverá atuar com a garra.
    Andar(-15.2)
    EsqCurva(90)
    Andar(31.9)
    EsqCurva(90)
    Andar(63)
    EsqCurva(90)
    Andar(34.3)
    EsqCurva(90)
    Andar(17.1)



elif sequencia == 'YGR':
    pass
elif sequencia == 'RYG':
    pass
elif sequencia == 'RGY':
    pass
elif sequencia == 'GRY':
    pass
elif sequencia == 'GYR':
    pass
