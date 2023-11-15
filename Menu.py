class Menu:
    def mostrarTitulo(self, titulo):
        print(f"======== {titulo} ========")
    
    def mostrarMenuUsuario(self):
        while True:
            self.mostrarTitulo("Menu Usuario")
            print("1 - Inserir novo usuario")
            print("2 - Visualizar todos os usuarios")
            print("3 - Visualizar usuarios ordenados por nome")
            print("4 - Sair\n")
            try:
                opcao = int(input("Digite uma opcao: "))
                if opcao == 1:
                    print("ola")
                elif opcao == 4:
                    break
            except ValueError:
                print("Digite um valor inteiro.")

    def mostrarMenuLivro(self):
        print("ola")
    
    def mostrarMenuEmprestimo(self):
        print("ola")
    
    def mostrarMenuRelatorios(self):
        print("ola")

    def mostrarMenuGeral(self):
        while True:
            self.mostrarTitulo("Menu Geral")
            print("1 - Usuario")
            print("2 - Livro")
            print("3 - Emprestimo")
            print("4 - Relatorios")
            print("5 - Sair\n")
            try:
                opcao = int(input("Digite uma opcao: "))
                if opcao == 1:
                    self.mostrarMenuUsuario()
                elif opcao == 2:
                    self.mostrarMenuLivro()
                elif opcao == 3:
                    self.mostrarMenuEmprestimo()
                elif opcao == 4:
                    self.mostrarMenuRelatorios()
                elif opcao == 5:
                    return
            except ValueError:
                print("Digite um valor inteiro.")

    