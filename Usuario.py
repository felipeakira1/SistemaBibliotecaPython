class Usuario:
    id = 1
    def __init__(self, nome, email, senha):
        self.id = Usuario.id
        Usuario.id += 1
        self.nome = nome
        self.email = email
        self.senha = senha
        self.historico = {}