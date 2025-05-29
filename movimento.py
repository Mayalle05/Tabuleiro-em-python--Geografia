import pygame
import sys

# Inicializa o Pygame
pygame.init()

# Carrega a imagem do tabuleiro
imagem_tabuleiro = pygame.image.load("tabuleiro.jpeg")
largura, altura = imagem_tabuleiro.get_size()

# Cria a janela com o mesmo tamanho da imagem
window = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Clique no Tabuleiro")

# Loop principal
rodando = True
while rodando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            x, y = evento.pos
            print(f"Clicado em: x={x}, y={y}")

    window.blit(imagem_tabuleiro, (0, 0))
    pygame.display.flip()

pygame.quit()
sys.exit()
