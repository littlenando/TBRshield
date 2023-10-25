from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase
from pybricks.tools import wait, StopWatch

hub        = PrimeHub()
esquerdo   = Motor(Port.F, Direction.COUNTERCLOCKWISE)
direito    = Motor(Port.B)
garra      = Motor(Port.C, Direction.COUNTERCLOCKWISE)
sobe       = Motor(Port.D)
mover      = GyroDriveBase(esquerdo, direito, 68.8, 113)
sensoresq  = ColorSensor(Port.A)
sensordir  = ColorSensor(Port.E)

def seleciona(cor):
    if cor == Color.RED:
        return("R")
    if cor == Color.GREEN:
        return("G")
    if cor == Color.YELLOW:
        return("Y")  

def andar(distancia, velocidade=240):
    mover.settings(velocidade, 900, 203, 913)
    mover.straight(distancia*10)

def curva(graus):
    mover.turn(graus)

def subir():
    sobe.run_time(10000,850, wait=False)

def descer():
    sobe.run_time(-1000, 850,)

def abre():
    garra.run_time(350, 1000)

def fecha():
     garra.run_time(-1000, 1000)

curva(90)
andar(40)
curva(-90)
subir()
andar(-68,350)
curva(-90)

cores = [Color.RED, Color.GREEN, Color.YELLOW]

while (sensordir.color() not in cores) and (sensoresq.color() not in cores):
    mover.drive(200,0)
mover.stop()
andar(1.3)

if sensordir.color() not in cores:
    cor3 = sensoresq.color()
else:
    cor3 = sensordir.color()

andar(-3)
curva(-90)

while (sensordir.color() not in cores) and (sensoresq.color() not in cores):
    mover.drive(200,0)
mover.stop()
andar(1.3)

if sensordir.color() not in cores:
    cor2 = sensoresq.color()
else:
    cor2 = seleciona(sensordir.color())


print(cor3)
print(cor2)
