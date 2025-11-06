import pygame
from pathlib import Path

# --- Configurações do labirinto ---
TAMANHO_CELULA = 800//25

img = Path("img")  

tile_grass = pygame.transform.scale(
    pygame.image.load(img / "tile-grass.png"),
    (int(TAMANHO_CELULA), int(TAMANHO_CELULA))
)

tile_wood = pygame.transform.scale(
    pygame.image.load(img / "tile-wood.png"),
    (int(TAMANHO_CELULA), int(TAMANHO_CELULA))
)

TAMANHO_JOGADOR = int(TAMANHO_CELULA * 0.9)

jogador_img = pygame.image.load(img / "gato.png")  
jogador_img = pygame.transform.smoothscale(
    jogador_img,
    (TAMANHO_JOGADOR, TAMANHO_JOGADOR)
)

# MAPA FÁCIL
LABIRINTO_FACIL = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,0,1,0,0,0,1,0,0,1,0,0,0,1,1,0,1,1,1,1,1],
    [1,1,1,1,1,0,1,0,1,0,1,0,1,1,1,1,0,1,1,0,1,1,1,1,1],
    [1,1,1,1,1,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,1,1,1,1,1],
    [1,1,1,1,1,1,1,0,1,1,1,1,1,1,0,1,1,1,1,0,1,1,1,1,1],
    [1,1,1,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,1,1,1,1,1],
    [1,1,1,1,1,0,1,1,1,1,0,1,0,1,1,1,1,0,0,0,1,1,1,1,1],
    [1,1,1,1,1,0,1,0,0,0,0,1,0,0,0,0,1,0,1,1,1,1,1,1,1],
    [1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,1,1],
    [1,1,1,1,1,0,0,0,0,0,0,0,1,0,1,0,0,0,1,0,1,1,1,1,1],
    [1,1,1,1,1,1,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,1,1],
    [1,1,1,1,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,1,1,1,1,1],
    [1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,1,1,2,1,1,1,1],
    [1,1,1,1,1,0,1,1,1,1,1,0,1,0,1,0,1,0,1,0,0,1,1,1,1],
    [1,1,1,1,1,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]


# MAPA MÉDIO
LABIRINTO_MEDIO = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,1,1],
    [1,1,1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,0,1,0,1,1,1],
    [1,1,0,0,0,0,0,1,0,1,0,0,0,1,0,0,0,1,0,0,1,0,0,1,1],
    [1,1,0,1,1,1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,0,1,1],
    [1,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,1],
    [1,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,1],
    [1,1,0,0,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,1],
    [1,1,0,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,1],
    [1,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,1,1],
    [1,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,1,1,1],
    [1,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,1],
    [1,1,0,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,1],
    [1,1,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,1,0,0,1,1],
    [1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,0,1,1,1],
    [1,1,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,1,1],
    [1,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,1],
    [1,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,1,1],
    [1,1,0,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,0,1,0,1,1],
    [1,1,0,0,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,1,1],
    [1,1,1,1,0,1,1,1,1,1,0,1,1,1,1,1,0,1,1,1,0,1,2,1,1],
    [1,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]



# MAPA DIFÍCIL
LABIRINTO_DIFICIL = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,1,1],
    [1,1,1,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,1],
    [1,1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,1,1],
    [1,1,0,1,0,1,1,1,0,1,0,1,0,1,1,1,0,1,1,1,1,1,0,1,1],
    [1,1,0,1,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0,0,0,0,0,1,1],
    [1,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,1],
    [1,1,0,1,0,1,0,1,0,1,0,0,0,1,0,0,0,0,0,0,0,1,0,1,1],
    [1,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,1,1,1,1,0,1,0,1,1],
    [1,1,0,0,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,1,1],
    [1,1,0,1,1,1,0,1,1,1,1,1,1,1,1,1,1,1,0,1,1,1,0,1,1],
    [1,1,0,0,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,1],
    [1,1,1,1,0,1,1,1,0,1,1,1,1,1,0,1,0,1,1,1,1,1,1,1,1],
    [1,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,0,1,0,0,0,0,0,1,1],
    [1,1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,0,1,0,1,1,1,0,1,1],
    [1,1,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0,1,0,1,0,0,0,1,1],
    [1,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,1,1,1],
    [1,1,0,1,0,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,1],
    [1,1,0,1,0,1,1,1,1,1,0,1,0,1,1,1,0,1,1,1,1,1,0,1,1],
    [1,1,0,1,0,1,0,1,0,0,0,1,0,0,0,0,0,1,0,0,0,1,0,1,1],
    [1,1,0,1,0,1,0,1,0,1,1,1,1,1,1,1,1,1,0,1,0,1,0,1,1],
    [1,1,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,2,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1],
]



# --- Fases ---
FASES = [LABIRINTO_FACIL, LABIRINTO_MEDIO, LABIRINTO_DIFICIL]
fase_atual = 0

# escolha padrão (pode trocar no jogo)
LABIRINTO = FASES[fase_atual]

def calcular_offset(tela):
    """Calcula o deslocamento para centralizar o labirinto na tela."""
    linhas = len(LABIRINTO)
    colunas = len(LABIRINTO[0])

    largura_total = colunas * TAMANHO_CELULA
    altura_total = linhas * TAMANHO_CELULA

    offset_x = (tela.get_width()  - largura_total) / 2
    offset_y = (tela.get_height() - altura_total) / 2

    return offset_x, offset_y

def encontrar_inicio():
    """Procura a primeira célula 0 do labirinto atual e retorna [linha, coluna]."""
    for i, row in enumerate(LABIRINTO):
        for j, v in enumerate(row):
            if v == 0:
                return [i, j]
    # fallback: se não houver 0, retorna o centro (evita crash)
    return [len(LABIRINTO)//2, len(LABIRINTO[0])//2]


def carregar_fase(indice):
    """Muda o labirinto para a fase indicada."""
    global LABIRINTO, fase_atual
    fase_atual = indice
    LABIRINTO = FASES[fase_atual]

# escolha padrão (pode trocar no jogo)
LABIRINTO = FASES[fase_atual]

def desenhar_labirinto(tela):
    offset_x, offset_y = calcular_offset(tela)

    for linha, row in enumerate(LABIRINTO):
        for coluna, cell in enumerate(row):
            x = int(offset_x + coluna * TAMANHO_CELULA)
            y = int(offset_y + linha  * TAMANHO_CELULA)

            if cell == 1:
                tela.blit(tile_grass, (x, y))
            else:
                tela.blit(tile_wood, (x, y))




# --- Configurações do jogador ---
POS_INICIAL = encontrar_inicio()

def desenhar_jogador(tela, posicao):
    linha, coluna = posicao
    offset_x, offset_y = calcular_offset(tela)

    # centraliza o gatinho dentro da célula
    margem = (TAMANHO_CELULA - TAMANHO_JOGADOR) // 2

    x = int(offset_x + coluna * TAMANHO_CELULA + margem)
    y = int(offset_y + linha  * TAMANHO_CELULA + margem)

    tela.blit(jogador_img, (x, y))


def posicao_valida(linha, coluna):
    """Retorna True se a posição está dentro do labirinto e não é parede."""
    if linha < 0 or linha >= len(LABIRINTO):
        return False
    if coluna < 0 or coluna >= len(LABIRINTO[0]):
        return False
    return LABIRINTO[linha][coluna] != 1
