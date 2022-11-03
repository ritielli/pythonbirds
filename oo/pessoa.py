class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=31):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
    def metodo_estatico():
        return  50

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'

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
    ritielli.sobrenome = 'Castro'
    del pedro.filhos
    ritielli.olhos = 1
    del ritielli.olhos
    print(ritielli.__dict__)
    print(pedro.__dict__)
    Pessoa.olhos = 3
    print(Pessoa.olhos)
    print(ritielli.olhos)
    print(pedro.olhos)
    print(id(Pessoa.olhos), id(ritielli.olhos), id(pedro.olhos))
    print(Pessoa.metodo_estatico(), ritielli.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), ritielli.nome_e_atributos_de_classe())