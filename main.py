from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ColorSensor, UltrasonicSensor, ForceSensor
from pybricks.parameters import Button, Color, Direction, Port, Side, Stop
from pybricks.robotics import DriveBase
from pybricks.tools import wait, StopWatch

#Declaração dos objetos do código

tempo     = StopWatch()
direito   = Motor(Port.B)
garra     = Motor(Port.C, Direction.COUNTERCLOCKWISE)
esquerdo  = Motor(Port.D, Direction.COUNTERCLOCKWISE)
corD      = ColorSensor(Port.E)
corE      = ColorSensor(Port.F)
fechar    = Motor(Port.A, Direction.COUNTERCLOCKWISE)
robo      = DriveBase(direito, esquerdo, 87.2, 127.4)
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
    if hub.imu.ready() == True:
        while hub.imu.heading() < (ang):
            esquerdo.run(100)
            direito.run(-100)
        esquerdo.brake()
        direito.brake()
        hub.imu.reset_heading(0)

def EsqCurva(ang):
    """
    Fez com que a DriveBase realize uma curva em seu próprio eixo para esquerda, com a angulação definida.

    Args:
        ang (float): ângulo da curva a ser realizado, em graus.
    """
    if hub.imu.ready() == True:
        while hub.imu.heading() > -(ang):
            esquerdo.run(-100)
            direito.run(100)
        esquerdo.brake()
        direito.brake()
        hub.imu.reset_heading(0)

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
garra.run_time(350,1800)
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

if sequencia == 'RGY': # Vermelho, verde e amarelo.
    garra.run_time(-350,1300)
    while corD.color() != Color.RED:
        robo.drive(130, 0)
    robo.stop()
    fechar.run_time(-140, 3000) #Pega as árvores vermelhas
    garra.run_time(400,2500)
    DirCurva(90)
    while corD.color() != Color.YELLOW:
        robo.drive(120,0) 
    robo.stop() #Vai até a Área de Reflorestamento Norte
    Andar(6)
    garra.run_time(-350,1300)
    fechar.run_time(130,2800)
    garra.run_time(350,2500) #Entrega as árvores vermelhas
    Andar(-8.5)
    garra.run_time(-350,1300)
    fechar.run_time(-140,3200)
    Andar(-6)
    fechar.run_time(-140,1300)
    garra.run_time(350,2500)
    DirCurva(90)
    Andar(68)
    EsqCurva(90)
    garra.run_time(350,2500)
    Andar(24)
    Andar(-6.4)
    garra.run_time(-350,2000)
    fechar.run_time(130,3000)
    garra.run_time(350,2500)
    Andar(-17)
    EsqCurva(90)
    garra.run_time(-350,1900)
    Andar(68)
    EsqCurva(90)
    while corD.color() != Color.GREEN:
        robo.drive(130,0)
    robo.stop()
    fechar.run_time(-140, 3000)
    garra.run_time(400,2500)
    Andar(-18)
    robo.turn(90)
    Andar(36)
    robo.turn(-90)
    hub.imu.reset_heading(0)
    garra.run_time(-100,1000)

elif sequencia == 'RYG':
    garra.run_time(-350,1500)
    while corD.color() != Color.RED:
        robo.drive(130, 0)
    robo.stop()
    fechar.run_time(-130, 3000)
    garra.run_time(400,2000)
    DirCurva(90)
    while corD.color() != Color.YELLOW:
        robo.drive(120,0)
    robo.stop()
    Andar(4.5)
    garra.run_time(-350,1300)
    fechar.run_time(130,2800)
    garra.run_time(350,3600)
    Andar(-12)
    DirCurva(180)
    garra.run_time(-350,1300)
    while corD.color() != Color.GREEN:
        robo.drive(130,0)
    robo.stop()
    fechar.run_time(-130,2600)
    garra.run_time(350,3600)
    Andar(-7)
    EsqCurva(90)
    Andar(70)
    EsqCurva(90)
    Andar(31)
    Andar(-6.6)
    garra.run_time(-350,1300)
    fechar.run_time(130,2300)
    garra.run_time(350,3600)
    Andar(-28)
    robo.turn(90)
    garra.run_time(-350,1100)
    while corD.color() != Color.RED:
        robo.drive(215,0)
    robo.stop()
    robo.turn(-90)
    while corD.color() != Color.YELLOW:
        robo.drive(130,0)
    robo.stop()
    Andar(-4)
    fechar.run_time(-130, 2800)
    Andar(-10)
    garra.run_time(350,3600)
    Andar(-10)
    robo.turn(-90)
    Andar(30)
    robo.turn(-90)
    garra.run_time(-200,1000)

elif sequencia == 'YGR':
    garra.run_time(-350,1500)
    while corD.color() != Color.RED:
        robo.drive(130, 0)
    robo.stop()
    fechar.run_time(-130, 3000)
    garra.run_time(400,2000)
    Andar(-67)
    DirCurva(90)
    Andar(23)
    Andar(-6)
    garra.run_time(-350,1500)
    fechar.run_time(130,3000)
    garra.run_time(350,1500)
    Andar(-17)
    EsqCurva(90)
    garra.run_time(-350,1500)
    while corD.color() != Color.RED:
        robo.drive(200, 0)
    robo.stop()
    DirCurva(90)
    while corD.color() != Color.YELLOW:
        robo.drive(200,0)
    robo.stop()
    Andar(-3.5)
    fechar.run_time(-130,2900)
    Andar(-3)
    fechar.run_time(-130,1000)
    garra.run_time(350,3800)
    Andar(20)
    Andar(-6.5)
    garra.run_time(-350,2000)
    fechar.run_time(130,2500)
    garra.run_time(400,2500)
    Andar(-10)
    DirCurva(180)
    garra.run_time(-350,2000)
    while corD.color() != Color.GREEN:
        robo.drive(130,0)
    robo.stop()
    fechar.run_time(-130, 3000)
    garra.run_time(400,2000)
    Andar(-18)
    robo.turn(90)
    Andar(35)
    robo.turn(-90)
    hub.imu.reset_heading(0)
    garra.run_time(-200,1000)

elif sequencia == 'YRG':
    while corD.color() != Color.RED:
        robo.drive(130,0)
    robo.stop()
    Andar(-3)
    DirCurva(90)
    garra.run_time(-350,1800)
    Andar(12)
    fechar.run_time(-135,2900)
    Andar(-5)
    fechar.run_time(-130,1000)
    garra.run_time(350,2000)
    Andar(22)
    Andar(-7)
    garra.run_time(-350,1000)
    fechar.run_time(130,2300)
    garra.run_time(350,2000)
    Andar(-8)
    DirCurva(180)
    garra.run_time(-350,1000)
    while corD.color() != Color.GREEN:
        robo.drive(130,0)
    robo.stop()
    fechar.run_time(-130,2800)
    garra.run_time(350,3800)
    Andar(-4)
    EsqCurva(90)
    Andar(64.5)
    EsqCurva(90)
    Andar(31)
    Andar(-6)
    garra.run_time(-350,1500)
    fechar.run_time(130,2850)
    garra.run_time(350,3800)
    Andar(-23)
    robo.turn(90)
    garra.run_time(-350,1300)
    while corD.color() != Color.RED:
        robo.drive(180,0)
    robo.stop()
    fechar.run_time(-130,3200)
    Andar(-6)
    fechar.run_time(-100,1000)
    garra.run_time(350,2300)
    Andar(-26)
    robo.turn(90)
    garra.run_time(-200,1000)

elif sequencia == 'GRY':
    while corD.color() != Color.RED:
        robo.drive(130,0)
    robo.stop()
    Andar(-3)
    DirCurva(90)
    garra.run_time(-350,1500)
    Andar(11)
    fechar.run_time(-135,2900)
    Andar(-5)
    fechar.run_time(-130,1000)
    garra.run_time(350,2000)
    DirCurva(90)
    Andar(68)
    EsqCurva(90)
    wait(100)
    robo.stop()
    esquerdo.run_time(220, 2000, wait=False)
    direito.run_time(220, 2000, wait=True)
    wait(200)
    Andar(-6)
    garra.run_time(-350,2000)
    fechar.run_time(150,2000)
    garra.run_time(350,2000)
    Andar(-13)
    EsqCurva(90)
    while corD.color() != Color.RED:
        robo.drive(220,0)
    robo.stop()
    Andar(-1.5)
    EsqCurva(90)
    garra.run_time(-350,1800)
    Andar(11)
    fechar.run_time(-150,1900)
    garra.run_time(350,2000)
    EsqCurva(180)
    wait(100)
    robo.stop()
    wait(200)
    esquerdo.run_time(220, 3500, wait=False)
    direito.run_time(220, 3500, wait=True)
    Andar(-6)
    garra.run_time(-350,1800)
    fechar.run_time(150,1900)
    garra.run_time(350,2000)
    Andar(-22)
    EsqCurva(90)
    Andar(-6)
    garra.run_time(-350,1700)
    Andar(9)
    fechar.run_time(-150,3000)
    garra.run_time(300,2000)
    Andar(-34)
    robo.turn(90)
    wait(500)
    garra.run_time(-200,1000)
    hub.imu.reset_heading(0)

elif sequencia == 'GYR':
    garra.run_time(-350,1500)
    while corD.color() != Color.RED:
        robo.drive(130, 0)
    robo.stop()
    fechar.run_time(-130, 3000)
    garra.run_time(400,2000)
    Andar(-68)
    DirCurva(90)
    Andar(25.7)
    Andar(-6.6)
    garra.run_time(-350,1500)
    fechar.run_time(130,3000)
    garra.run_time(350,1500)
    Andar(-17)
    EsqCurva(90)
    garra.run_time(-350,1500)
    while corD.color() != Color.RED:
        robo.drive(200, 0)
    robo.stop()
    EsqCurva(90)
    Andar(9)
    fechar.run_time(-130,3300)
    garra.run_time(350,3800)
    DirCurva(180)
    while corD.color() != Color.YELLOW:
        robo.drive(120,0)
    robo.stop()
    Andar(6)
    garra.run_time(-350,1500)
    fechar.run_time(130,2800)
    garra.run_time(350,3800)
    Andar(-8)
    garra.run_time(-350,1500)
    fechar.run_time(-130,3200)
    garra.run_time(-130,3000)
    Andar(-6)
    fechar.run_time(-130,2200)
    garra.run_time(350,3800)
    robo.turn(-90)
    Andar(30)
    robo.turn(-90)
    garra.run_time(-300,1000)

#Sobe a rampa vai pro outro lado (Comum etc)
robo.settings(630,1141,100,800)
while not(direito.stalled()):
    robo.drive(-640,0)
robo.stop()
robo.settings(300,1141,80,800)
Andar(4)
robo.turn(90)
wait(300)
garra.run_time(300,1500)
while corD.color() != Color.GREEN and corE.color() != Color.GREEN:
    robo.drive(200,0)
robo.stop()
Andar(14.2)
robo.turn(90)
Andar(40.5)
robo.turn(60)
Andar(9)
while not(corD.color() == Color.BLUE and corE.color() == Color.BLUE):
    robo.drive(200,0)
robo.stop()
Andar(13.5)
garra.run_time(350,1800)
robo.turn(120)
while not(direito.stalled()):
    robo.drive(300,0)
Andar(-7)
garra.run_time(-350,1400)
fechar.run_time(140,1800)
garra.run_time(350,1800)
Andar(-9)
wait(1000)

print('O programa foi executado em: ', tempo.time()/1000, 's')
