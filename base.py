import pygame
from pathlib import Path

# --- Configurações do labirinto ---
TAMANHO_CELULA = 800/17

img = Path("img")  

tile_grass = pygame.transform.scale(
    pygame.image.load(img / "tile-grass.png"),
    (TAMANHO_CELULA, TAMANHO_CELULA)
)

tile_wood = pygame.transform.scale(
    pygame.image.load(img / "tile-wood.png"),
    (TAMANHO_CELULA, TAMANHO_CELULA)
)

# COR_PAREDE = (70, 70, 200)
# COR_CAMINHO = (200, 200, 200)
# COR_SAIDA = (80, 200, 120)

# MAPA FÁCIL
LABIRINTO_FACIL =  [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,0,1,0,0,0,1,0,0,1,0,0,0,1,1,0,1],
    [1,0,1,0,1,0,1,0,1,1,1,1,0,1,1,0,1],
    [1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1],
    [1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1],
    [1,0,1,1,1,1,0,1,0,1,1,1,1,0,0,0,1],
    [1,0,1,0,0,0,0,1,0,0,0,0,1,0,1,1,1],
    [1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,0,1],
    [1,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,1],
    [1,1,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1],
    [1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1],
    [1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1],
    [1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,0,1],
    [1,0,1,1,1,1,1,0,1,1,1,0,1,0,1,0,1],
    [1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]

# MAPA MÉDIO
LABIRINTO_MEDIO = [
    [1,1,1,1,1,1,1,1,1],
    [1,0,0,1,0,0,0,0,1],
    [1,0,1,1,1,1,0,1,1],
    [1,0,1,0,0,0,0,0,1],
    [1,0,1,0,1,1,1,0,1],
    [1,0,0,0,0,0,1,0,1],
    [1,1,1,1,1,0,1,2,1],
    [1,1,1,1,1,1,1,1,1],
]

# MAPA DIFÍCIL
LABIRINTO_DIFICIL = [
    [1,1,1,1,1,1,1,1,1,1,1],
    [1,0,0,0,1,0,0,0,0,2,1],
    [1,0,1,0,1,0,1,1,0,1,1],
    [1,0,1,0,0,0,1,0,0,0,1],
    [1,0,1,1,1,0,1,0,1,0,1],
    [1,0,0,0,0,0,0,0,1,0,1],
    [1,1,1,1,1,1,1,0,1,0,1],
    [1,0,0,0,0,0,1,0,0,0,1],
    [1,0,1,1,1,0,1,1,1,0,1],
    [1,0,0,0,0,0,0,0,0,0,1],
    [1,1,1,1,1,1,1,1,1,1,1],
]

# escolha padrão (pode trocar no jogo)
LABIRINTO = LABIRINTO_FACIL

def desenhar_labirinto(tela):
    for linha, row in enumerate(LABIRINTO):
        for coluna, cell in enumerate(row):
            x = coluna * TAMANHO_CELULA
            y = linha * TAMANHO_CELULA

            if cell == 1:
                tela.blit(tile_grass, (x, y))  # parede
            else:  # 0 (caminho) ou 2 (saída, se você não tratar separado)
                tela.blit(tile_wood, (x, y))


# --- Configurações do jogador ---
COR_JOGADOR = (240, 230, 70)
POS_INICIAL = [1, 1]  # linha, coluna


def desenhar_jogador(tela, posicao):
    """Desenha o jogador (quadrado amarelo) na posição atual."""
    linha, coluna = posicao
    x = coluna * TAMANHO_CELULA + 5
    y = linha * TAMANHO_CELULA + 5
    tamanho = TAMANHO_CELULA - 10
    pygame.draw.rect(tela, COR_JOGADOR, (x, y, tamanho, tamanho))


def posicao_valida(linha, coluna):
    """Retorna True se a posição está dentro do labirinto e não é parede."""
    if linha < 0 or linha >= len(LABIRINTO):
        return False
    if coluna < 0 or coluna >= len(LABIRINTO[0]):
        return False
    return LABIRINTO[linha][coluna] != 1
