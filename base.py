import pygame

# --- Configurações do labirinto ---
TAMANHO_CELULA = 50
COR_PAREDE = (70, 70, 200)
COR_CAMINHO = (200, 200, 200)

LABIRINTO = [
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,],
    [1,0,0,0,0,0,1,0,0,0,0,1,0,0,1,],
    [1,0,1,1,1,0,1,0,1,1,0,1,0,0,1,],
    [1,0,1,0,0,0,0,0,1,0,0,0,1,0,1,],
    [1,0,1,0,1,1,1,0,1,1,1,0,1,0,1,],
    [1,0,0,0,0,0,1,0,0,0,1,0,0,0,1,],
    [1,1,1,1,1,0,1,1,1,0,1,1,1,0,1,],
    [1,0,0,0,1,0,0,0,1,0,0,0,1,0,1,],
    [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,],
]

def desenhar_labirinto(tela):
    """Desenha o labirinto na tela."""
    for linha, row in enumerate(LABIRINTO):
        for coluna, cell in enumerate(row):
            x = coluna * TAMANHO_CELULA
            y = linha * TAMANHO_CELULA
            cor = COR_PAREDE if cell == 1 else COR_CAMINHO
            pygame.draw.rect(tela, cor, (x, y, TAMANHO_CELULA, TAMANHO_CELULA))

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

