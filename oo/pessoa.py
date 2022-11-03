class Pessoa:
    def __init__(self, *filhos, nome=None, idade=31):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    pedro = Pessoa(nome='Pedro')
    ritielli = Pessoa(pedro, nome='Ritielli')
    print(Pessoa.cumprimentar(ritielli))
    print(id(ritielli))
    print(ritielli.cumprimentar())
    print(ritielli.nome)
    print(ritielli.idade)
    for filho in ritielli.filhos:
        print(filho.nome)