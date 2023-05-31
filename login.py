from passlib.hash import pbkdf2_sha256 as cryp

class Usuario:
    contador = 0
    def __init__(self, nome, sobrenome, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.sobrenome = sobrenome
        self.__senha = cryp.hash(senha, rounds=200000, salt_size=16)
        Usuario.contador = self.__id

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False


nome = input("Digite seu nome: ")
sobrenome = input("Digite seu sobrenome: ")
print("Sua senha deve conter 4 dígitos")
senha = input("Digite sua senha: ")

while len(senha) != 4:
    print("*** Digite uma senha de 4 dígitos ***\n")
    senha = input("Digite sua senha: ")

confirma_senha = input("Confirme sua senha: ")

if senha == confirma_senha:
    user = Usuario(nome, sobrenome, senha)
    print("Usuário criado com sucesso!\n")
else:
    print("Senha não confere!")
    exit(33)

login = input("Digite seu login: ")

if login == nome:
    senha = input("Digite sua senha para acessar: ")
else:
    print("Login não confere!")
    exit(33)

if user.checa_senha(senha):
    print("Acesso Concedido!")
else:
    print("Acesso Negado!")

