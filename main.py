from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import GyroDriveBase
from pybricks.tools import wait, StopWatch

#Declaração dos objetos do código

tempo     = StopWatch()
direito   = Motor(Port.B)
fechar    = Motor(Port.C, Direction.COUNTERCLOCKWISE)
garra     = Motor(Port.D, Direction.CLOCKWISE)
corD      = ColorSensor(Port.A)
corE      = ColorSensor(Port.E)
esquerdo  = Motor(Port.F, Direction.COUNTERCLOCKWISE)
robo      = GyroDriveBase(esquerdo, direito, 70, 127.4)
hub       = PrimeHub()

print('Bateria (em mV): ', hub.battery.voltage())
robo.settings(330,1141,100,800) # Define respectivamente: velocidade, aceleração, velocidade de curva e aceleração de curva
hub.light.on(Color.RED)
hub.imu.reset_heading(0)

#Ínicio do código
def SelecionaCor(cor):
    """
    Retorna uma string com a inicial da cor. Ex.: Para o objeto Color.RED retorna a string 'R'.

    Args:
        cor (Color): cor a ser convertida
    Retorna:
        (string): cor convertida em string
    """
    if cor == Color.RED:
        return('R')
    if cor == Color.GREEN:
        return('G')
    if cor == Color.YELLOW:
        return('Y')

def DirCurva(ang):
    """
    Fez com que a DriveBase realize uma curva em seu próprio eixo para direita, com a angulação definida.

    Args:
        ang (float): ângulo da curva a ser realizado, em graus.
    """
    robo.turn(ang)

def EsqCurva(ang):
    """
    Fez com que a DriveBase realize uma curva em seu próprio eixo para esquerda, com a angulação definida.

    Args:
        ang (float): ângulo da curva a ser realizado, em graus.
    """
    robo.turn(-ang)

def Andar(cm):
    """
    Fez com que a DriveBase ande em linha reta por uma distância determinada.

    Args:
        cm (float): distância em centímetros a ser percorrida pelo robô.
    """
    robo.straight(cm*10)

def Estaciona():
    """
    Alinha o robô com uma linha reta da cor preta.
    """
    while corD.reflection() > 5 and corE.reflection() > 5:
        robo.drive(50,0)
    robo.stop()
    if corD.reflection() < 5:
        while corE.reflection() > 5:
            direito.run(90)
        wait(150)
        direito.brake()
    elif corE.reflection() < 5:
        while corD.reflection() > 5:
            esquerdo.run(90)
        wait(150)
        esquerdo.brake()

#Chegada até o ponto central da rampa (comum a todos)

DirCurva(90)
garra.run_time(350,1000)
Andar(38)
DirCurva(90)
robo.stop()
robo.settings(450,1141,100,800) # Aumenta a velocidade do robô para subir na rampa com mais precisão.

Andar(61)
robo.stop()
robo.settings(320,1141,100,800)


cores = [Color.GREEN, Color.RED, Color.YELLOW] #Lista com cores possíveis para as plaquetas

while corD.color() not in cores and corE.color() not in cores:
    robo.drive(95,0)
robo.stop()
Andar(2)
wait(450)
#Seleciona a cor da frente, dando prioridade para o sensor direito.
if corD.color() == Color.NONE:
    cor2 = SelecionaCor(corE.color())
else:
    cor2 = SelecionaCor(corD.color())
Andar(-5)
DirCurva(90)
while corD.color() not in cores and corE.color() not in cores:
    robo.drive(95,0)
Andar(2)
wait(500)
if corE.color() == Color.NONE:
    cor3 = SelecionaCor(corD.color())
else:
    cor3 = SelecionaCor(corE.color())

#Deduz a terceira cor com base nas outras cores.
if cor3 != 'Y' and cor2 != 'Y':
    cor1 = SelecionaCor(Color.YELLOW)
elif cor3 != 'G' and cor2 != 'G':
    cor1 = SelecionaCor(Color.GREEN)
else:
    cor1 = SelecionaCor(Color.RED)
sequencia = f'{cor1}{cor2}{cor3}' # Descobre a sequência executada
print(f'A sequência executada é: {sequencia}')
Andar(-7)
DirCurva(90)
Andar(35)

if corD.reflection() < 5:
    while corD.reflection() < 5:
        esquerdo.run(100)
    esquerdo.brake()
if corE.reflection() < 5:
    while corE.reflection() < 5:
        direito.run(100)
    direito.brake()

Andar(21)
Estaciona()
Andar(4)
DirCurva(90)
Andar(11)

# Início da rotina de programação escolhida


    
print('O programa foi executado em: ', tempo.time()/1000, 's')
