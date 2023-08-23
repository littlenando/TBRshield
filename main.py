from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

direito = Motor(Port.B)
garra = Motor(Port.C, Direction.COUNTERCLOCKWISE)
esquerdo = Motor(Port.D, Direction.COUNTERCLOCKWISE)
corD = ColorSensor(Port.E)
corE = ColorSensor(Port.F)
fechar = Motor(Port.A)

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

DirCurva(90)
garra.run_time(350,1500)
Andar(40)
DirCurva(90)
Andar(61.5)

cores = [Color.GREEN, Color.RED, Color.YELLOW]

while corD.color() not in cores and corE.color() not in cores:
    robo.drive(95,0)
robo.stop()
Andar(0.2)
if corD.color() == Color.NONE:
    cor2 = SelecionaCor(corE.color())
else:
    cor2 = SelecionaCor(corD.color())
Andar(-5)
DirCurva(90)
while corD.color() not in cores and corE.color() not in cores:
    robo.drive(95,0)
Andar(0.3)
cor3 = SelecionaCor(corD.color())

if cor3 != 'Y' and cor2 != 'Y':
    cor1 = SelecionaCor(Color.YELLOW)
elif cor3 != 'G' and cor2 != 'G':
    cor1 = SelecionaCor(Color.GREEN)
else:
    cor1 = SelecionaCor(Color.RED)
sequencia = f'{cor1}{cor2}{cor3}'
print(f'A sequência executada é: {sequencia}')
DirCurva(90)
Andar(35)

if corD.reflection() < 6:
    while corD.reflection() < 6:
        esquerdo.run(100)
    esquerdo.brake()
if corE.reflection() < 6:
    while corE.reflection() < 6:
        direito.run(100)
    direito.brake()

Andar(20)
Estaciona()
Andar(4)
DirCurva(90)
Andar(11)

if sequencia == 'RGY':
    pass
elif sequencia == 'RYG':
    pass
elif sequencia == 'YGR':
    garra.run_time(-350,1500)
    while corD.color() != Color.RED:
        robo.drive(130, 0)
    robo.stop()
    fechar.run_time(-100, 3000)
    garra.run_time(400,2000)
    Andar(-68)
    DirCurva(90)
    Andar(23)
    Andar(-4.6)
    garra.run_time(-350,1500)
    fechar.run_time(100,3000)
    garra.run_time(350,1500)
    Andar(-17)
    EsqCurva(90)
    garra.run_time(-350,1500)
    while corD.color() != Color.RED:
        robo.drive(200, 0)
    robo.stop()
    DirCurva(90)
    Andar(13)
    fechar.run_time(-100,2900)
    garra.run_time(350,3800)
    Andar(21)
    Andar(-5.7)
    garra.run_time(-350,2000)
    fechar.run_time(100,2500)
    garra.run_time(400,2500)
    Andar(-10)
    DirCurva(180)
    garra.run_time(-350,2000)
    while corD.color() != Color.GREEN:
        robo.drive(130,0)
    robo.stop()
    fechar.run_time(-100, 3000)
    garra.run_time(400,2000)
    Andar(-18)
    EsqCurva(90)
    Andar(35)
    EsqCurva(90)
    while corD.color() != Color.RED:
        robo.drive(200,0)
    robo.stop()
    Estaciona()
    Andar(50)


elif sequencia == 'YRG':
    pass
elif sequencia == 'GRY':
    pass
elif sequencia == 'GYR':
    pass
