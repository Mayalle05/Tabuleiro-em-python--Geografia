import random

def rolar_dado():
    dado = {
        1: (
            "┌───────┐",
            "│       │",
            "│   ●   │",
            "│       │",
            "└───────┘"
        ),
        2: (
            "┌───────┐",
            "│ ●     │",
            "│       │",
            "│     ● │",
            "└───────┘"
        ),
        3: (
            "┌───────┐",
            "│ ●     │",
            "│   ●   │",
            "│     ● │",
            "└───────┘"
        ),
        4: (
            "┌───────┐",
            "│ ●   ● │",
            "│       │",
            "│ ●   ● │",
            "└───────┘"
        ),
        5: (
            "┌───────┐",
            "│ ●   ● │",
            "│   ●   │",
            "│ ●   ● │",
            "└───────┘"
        ),
        6: (
            "┌───────┐",
            "│ ●   ● │",
            "│ ●   ● │",
            "│ ●   ● │",
            "└───────┘"
        )
    }

    numero = random.randint(1, 6)
    for linha in dado[numero]:
        print(linha)
    print(f"Você rolou um {numero}!\n")

while True:
    comando = input("Pressione Enter para rolar o dado ou digite 'sair' para encerrar: ")
    if comando.lower() == "sair":
        print("Encerrando o jogo. Até a próxima!")
        break
    rolar_dado()
