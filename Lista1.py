class Tamagotchi:
    def _init_(self, nome):
        self.nome = nome
        self.fome = 0
        self.felicidade = 100

    def alimentar(self):
        self.fome -= 20
        if self.fome < 0:
            self.fome = 0
        self.felicidade += 10
        if self.felicidade > 100:
            self.felicidade = 100
        print(f"{self.nome} foi alimentado!")

    def brincar(self):
        self.fome += 10
        if self.fome > 100:
            self.fome = 100
        self.felicidade += 20
        if self.felicidade > 100:
            self.felicidade = 100
        print(f"{self.nome} está feliz brincando!")

    def verificar_estado(self):
        print(f"{self.nome}: Fome = {self.fome}, Felicidade = {self.felicidade}")

# Criando um Tamagotchi
nome_tamagotchi = input("Digite o nome do seu Tamagotchi: ")
meu_tamagotchi = Tamagotchi(nome_tamagotchi)

# Interagindo com o Tamagotchi
while True:
    print("\nEscolha uma opção:")
    print("1. Alimentar")
    print("2. Brincar")
    print("3. Verificar estado")
    print("4. Sair")
    
    opcao = input("Digite o número da opção: ")
    
    if opcao == "1":
        meu_tamagotchi.alimentar()
    elif opcao == "2":
        meu_tamagotchi.brincar()
    elif opcao == "3":
        meu_tamagotchi.verificar_estado()
    elif opcao == "4":
        print("Até mais!")
        break
    else:
        print("Opção inválida. Escolha novamente.")