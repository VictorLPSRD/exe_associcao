class Escritor:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta

    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramenta = ferramenta


class FerramentaDeEscrever:
    def __init__(self, nome):
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo'


escritor = Escritor('Luiz')
caneta = FerramentaDeEscrever('Caneta Bic')
lapis= FerramentaDeEscrever('lapiz')
maquina_de_escrever = FerramentaDeEscrever('Máquina')
escritor.ferramenta = maquina_de_escrever
escritor.ferramenta= caneta
escritor.ferramenta= lapis

print(caneta.escrever())

print(maquina_de_escrever.escrever())
print(escritor.ferramenta.escrever())

#EXECICIO AULA 218 
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Carro:
    def __init__(self,nome):#1
        self.nome = nome
        self._motor = None
        self._fabrica = None

    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self,motor):
        self._motor= motor

    @property
    def fabrica(self):
        return self._fabrica
    
    @fabrica.setter
    def fabrica(self,fabrica):
        self._fabrica= fabrica


class Motor:#2
    def __init__(self,nome):
        self.nome= nome


class Fabricante:#3
    def __init__(self,nome):
        self.nome= nome

Carro1=Carro('hb20')
moto1=Motor('M1')
fabri=Fabricante('Honda')

Carro1.motor =moto1#4
Carro1.fabrica= fabri#5

Carro2=Carro('Corrola')
Carro2.motor =moto1
Carro2.fabrica= fabri


print('Nome= ',Carro1.nome, " MOTOR= ", Carro1.motor.nome,' FABRICANTE=',Carro1.fabrica.nome)
print()
print('Nome= ',Carro2.nome, " MOTOR= ", Carro2.motor.nome,' FABRICANTE=',Carro2.fabrica.nome)
