class Livro:
    id = 1

    def __init__(self, titulo, autor, ISBN):
        self.id = Livro.id
        Livro.id += 1
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.status = "Disponivel"

    def __str__(self):
        return f"{self.id}: {self.titulo} - {self.autor} ({self.status})"