import pygame
import sys
import random

# Inicializa o Pygame
pygame.init()

# Carrega o tabuleiro 
tabuleiro_img_original = pygame.image.load("start.png")
tabuleiro_img = pygame.transform.scale(tabuleiro_img_original, (1500, 800))  # ou o tamanho que você quiser
WIDTH, HEIGHT = 1500, 800
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tabuleiro com Peões Arrastáveis e Dado")

# Carrega as imagens dos peões
peao1_img = pygame.image.load("peao1_transparente.png")
peao2_img = pygame.image.load("peao2_transparente.png")
peao3_img = pygame.image.load("peao3_transparente.png")
peao4_img = pygame.image.load("peao4_transparente.png")

# Redimensiona os peões
peao1_img = pygame.transform.scale(peao1_img, (150, 150))
peao2_img = pygame.transform.scale(peao2_img, (150, 150))
peao3_img = pygame.transform.scale(peao3_img, (150, 150))
peao4_img = pygame.transform.scale(peao4_img, (150, 150))

# Lista com dados dos peões
peoes = [
    {"img": peao1_img, "pos": [10, HEIGHT - 90]},
    {"img": peao2_img, "pos": [100, HEIGHT - 90]},
    {"img": peao3_img, "pos": [10, HEIGHT - 180]},
    {"img": peao4_img, "pos": [100, HEIGHT - 180]},
]

# Variáveis de arrastar
peao_selecionado = None
offset_x = 0
offset_y = 0

# Função do dado com desenho bonito
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
    print(f"🎲 Você rolou um {numero}!\n")
    return numero

# Loop principal
clock = pygame.time.Clock()
running = True
while running:
    window.blit(tabuleiro_img, (0, 0))

    # Desenha os peões
    for peao in peoes:
        window.blit(peao["img"], peao["pos"])

    pygame.display.flip()
    clock.tick(60)

    # Eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Clique com mouse para arrastar peão
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:  # botão esquerdo
                mouse_x, mouse_y = event.pos
                for i, peao in enumerate(peoes):
                    px, py = peao["pos"]
                    if px <= mouse_x <= px + 80 and py <= mouse_y <= py + 80:
                        peao_selecionado = i
                        offset_x = mouse_x - px
                        offset_y = mouse_y - py
                        break

        # Arrastar o peão
        elif event.type == pygame.MOUSEMOTION:
            if peao_selecionado is not None:
                mouse_x, mouse_y = event.pos
                peoes[peao_selecionado]["pos"] = [mouse_x - offset_x, mouse_y - offset_y]

        # Soltar o peão
        elif event.type == pygame.MOUSEBUTTONUP:
            if event.button == 1:
                peao_selecionado = None

        # Rolar dado com tecla espaço
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                rolar_dado()

pygame.quit()
sys.exit()
