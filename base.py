import pygame
import sys

# Inicializa o Pygame
pygame.init()

# --- Configurações ---
LARGURA_TELA = 1400
ALTURA_TELA = 1200
TITULO_JOGO = "Labirinto"

# Cores (R, G, B)
COR_FUNDO = (30, 30, 30)

# Criação da janela
tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption(TITULO_JOGO)

# Controle de FPS
clock = pygame.time.Clock()

# Loop principal do jogo
rodando = True
while rodando:
    # Limita a 30 quadros por segundo
    clock.tick(30)

    # Eventos (fechar janela, teclas, etc.)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            rodando = False

    # Preenche a tela com a cor de fundo
    tela.fill(COR_FUNDO)

    # Atualiza a tela
    pygame.display.flip()

# Sai do jogo corretamente
pygame.quit()
sys.exit()
