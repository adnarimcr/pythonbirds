class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=None):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    rodrigo = Pessoa(nome='Rodrigo', idade=36)
    miranda = Pessoa(rodrigo, nome='Miranda', idade=66)
    print(Pessoa.cumprimentar(miranda))
    print(id(miranda))
    print(miranda.cumprimentar())
    print(miranda.nome)
    print(miranda.idade)
    for filho in miranda.filhos:
        print(filho.nome)
    rodrigo.sobrenome = 'Miranda'
    del miranda.filhos
    miranda.olhos = 1
    print(rodrigo.__dict__)
    print(miranda.__dict__)
    print(Pessoa.olhos)
    print(miranda.olhos)
    print(id(Pessoa.olhos), id(miranda.olhos), id(rodrigo.olhos))

