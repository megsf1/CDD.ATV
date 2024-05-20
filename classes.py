class Pessoa:
    def __init__(self, nome,peso,idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = False
        self.andando = False
        self.falando = False


    def comer(self, alimento):
        if self.comendo == False and self.andando == False and self.falando == False:
            print(f'{self.nome} está comendo {alimento}.')
            self.comendo = True
        elif self.falando == True or self.andando == True:
            print(f'{self.nome}, pare para poder comer.')
        else:
            print(f'{self.nome} já esta comendo.')


    def andar(self):
        if self.andando == False and self.comendo == False and self.falando == False:
            print(f'{self.nome} está andando. ')
            self.andando = True
        elif self.comendo == True or self.falando == True:
            print(f'{self.nome}, pare para andar.')
        else:
            print(f'{self.nome} já está andando.')


    def falar(self):
        if self.falando == False and self.comendo == False and self.andando == False:
           print(f'{self.nome} está falando.')
           self.falando = True
        elif self.andando == True or self.comendo == True:
            print(f'{self.nome}, pare para poder falar.')
        else:
            print(f'{self.nome} já está falando.')

    def pararcomer(self):
        if self.comendo == True:
             print(f'{self.nome} parou de comer.')
             self.comendo = False
        else:
            print(f'{self.nome} ja esta sem comer!')

    def pararAndar(self):
        if self.andando == True:
            print(f'{self.nome} parou de andar.')
            self.andando = False
        else:
            print(f'{self.nome} ja esta parado!')

    def pararfalar(self):
        if self.falando == True:
            print(f'{self.nome} parou de falar.')
            self.falando = False
        else:
            print(f'{self.nome} ja esta calado!')



