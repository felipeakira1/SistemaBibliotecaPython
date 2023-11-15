from Livro import Livro

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []
    
    def adicionarLivro(self, livro):
        if not isinstance(livro, Livro):
            raise TypeError("O argumento deve ser um objeto do tipo Livro")
        self.livros.append(livro)

    def removerLivroId(self, id):
        # Subtrair um de id pois a lista de livros começa com id = 1, enquanto o metodo pop começa sua procura pelo indice 0
        id -= 1
        self.livros.pop(id)
        
    def mostrarTodosLivros(self):
        print(f"Biblioteca {self.nome}")
        for livro in self.livros:
            print(livro)
        print('\n')

livro1 = Livro("Hunger Games", "Suzanne Collins", "978-1-234567-89-0")
livro2 = Livro("Hunger Games 2", "Suzanne Collins", "978-1-234567-89-0")
biblioteca = Biblioteca("Carlos Chagas")

try:
    biblioteca.adicionarLivro(livro1)
    biblioteca.adicionarLivro(livro2)
except TypeError:
    print("O argumento deve ser um objeto do tipo Livro")

biblioteca.mostrarTodosLivros()
biblioteca.removerLivroId(1)
biblioteca.mostrarTodosLivros()


