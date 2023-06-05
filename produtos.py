class Produtos:
    contador = 0

    def __init__(self, nome, tipo, marca, cor, cod_cor, espessura, peso, quantidade, valor):
        self.__id = Produtos.contador + 1
        self.__nome = nome
        self.__tipo = tipo
        self.__marca = marca
        self.__cor = cor
        self.__cod_cor = cod_cor
        self.__espessura = espessura
        self.__peso = peso
        self.__quantidade = quantidade
        self.__valor = valor

    def valor_total(self):
        return self.__valor * self.__quantidade

nome = input("Digite o nome do produto: ")
tipo = input("Digite o tipo do produto: ")
marca = input("Digite a marca do produto: ")
cor = input("Digite a cor do produto: ")
cod_cor = input("Digite o código do produto: ")
espessura = input("Digite a espessura do produto: ")
peso = float(input("Digite o peso do produto: "))
quantidade = int(input("Digite a quantidade do produto: "))
valor = float(input("Digite o valor do produto: "))

produto = Produtos(nome, tipo, marca, cor, cod_cor, espessura, peso, quantidade, valor)

print(f'O valor total do produto é R${produto.valor_total():.2f}')


