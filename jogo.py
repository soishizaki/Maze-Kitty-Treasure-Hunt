import pygame
import sys
from base import *  

# Inicializa o Pygame
pygame.init()

# --- Configurações da tela ---
LARGURA_TELA = 1400
ALTURA_TELA = 1200
TITULO_JOGO = "Labirinto"
COR_FUNDO = (30, 30, 30)

# Criação da janela
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption(TITULO_JOGO)

# Controle de FPS
clock = pygame.time.Clock()

# Loop principal do jogo
rodando = True
while rodando:
    clock.tick(30)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    tela.fill(COR_FUNDO)

    # Chama a função que desenha o labirinto
    desenhar_labirinto(tela)

    pygame.display.flip()

# Sai do jogo corretamente
pygame.quit()
sys.exit()
