import pygame
import sys
import base
from base import *

pygame.init()

# --- Configurações da tela ---
LARGURA_TELA = 800
ALTURA_TELA = 800
TITULO_JOGO = "Labirinto"
COR_FUNDO = (30, 30, 30)
COR_TEXTO = (255, 255, 255)
COR_BOTAO = (70, 70, 200)
COR_BOTAO_HOVER = (100, 100, 255)

tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption(TITULO_JOGO)
clock = pygame.time.Clock()


# --- Função para desenhar botão ---
def desenhar_botao(tela, texto, x, y, largura, altura, mouse_pos):
    fonte = pygame.font.SysFont(None, 60)
    rect = pygame.Rect(x, y, largura, altura)
    cor = COR_BOTAO_HOVER if rect.collidepoint(mouse_pos) else COR_BOTAO

    pygame.draw.rect(tela, cor, rect, border_radius=12)
    texto_img = fonte.render(texto, True, COR_TEXTO)
    texto_rect = texto_img.get_rect(center=rect.center)
    tela.blit(texto_img, texto_rect)
    return rect


# --- Tela de menu inicial ---
def menu_inicial():
    while True:
        mouse_pos = pygame.mouse.get_pos()
        tela.fill(COR_FUNDO)

        fonte_titulo = pygame.font.SysFont(None, 80, bold=True)
        titulo = fonte_titulo.render("Escolha a dificuldade", True, COR_TEXTO)
        tela.blit(titulo, (LARGURA_TELA // 2 - titulo.get_width() // 2, 180))

        centro_x = LARGURA_TELA // 2
        inicio_y = ALTURA_TELA // 2 - 100

        botao_facil = desenhar_botao(tela, "Fácil",   centro_x - 150, inicio_y,       300, 80, mouse_pos)
        botao_medio = desenhar_botao(tela, "Médio",   centro_x - 150, inicio_y + 130, 300, 80, mouse_pos)
        botao_dif   = desenhar_botao(tela, "Difícil", centro_x - 150, inicio_y + 260, 300, 80, mouse_pos)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                if botao_facil.collidepoint(mouse_pos):
                    carregar_fase(0)  # começa na fase fácil
                    return
                elif botao_medio.collidepoint(mouse_pos):
                    carregar_fase(1)  # começa no médio
                    return
                elif botao_dif.collidepoint(mouse_pos):
                    carregar_fase(2)  # começa no difícil
                    return

        pygame.display.flip()
        clock.tick(30)


# --- Tela de vitória: Próxima fase / Sair ---
def tela_vitoria():
    while True:
        mouse_pos = pygame.mouse.get_pos()
        tela.fill(COR_FUNDO)

        fonte_titulo = pygame.font.SysFont(None, 80, bold=True)
        titulo = fonte_titulo.render("VOCÊ VENCEU! 🏆", True, COR_TEXTO)
        tela.blit(titulo, (LARGURA_TELA // 2 - titulo.get_width() // 2, 200))

        centro_x = LARGURA_TELA // 2
        botao_prox = desenhar_botao(tela, "Próxima fase", centro_x - 200, 400, 400, 90, mouse_pos)
        botao_sair = desenhar_botao(tela, "Sair",          centro_x - 200, 520, 400, 90, mouse_pos)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.MOUSEBUTTONDOWN:
                # Se clicar em próxima fase
                if botao_prox.collidepoint(mouse_pos):
                    # Se ainda existe próxima fase
                    if base.fase_atual < len(base.FASES) - 1:
                        return "proxima"
                    else:
                        # se já é a última, tratar como sair
                        return "sair"

                # Se clicar em sair
                if botao_sair.collidepoint(mouse_pos):
                    return "sair"

        pygame.display.flip()
        clock.tick(30)


# --- Loop principal do jogo ---
def main():
    menu_inicial()  # escolhe a fase inicial (dificuldade)

    pos_jogador = base.encontrar_inicio()
    vitoria = False
    rodando = True

    while rodando:
        clock.tick(30)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            if evento.type == pygame.KEYDOWN and not vitoria:
                nova_linha, nova_coluna = pos_jogador

                if evento.key == pygame.K_UP:
                    nova_linha -= 1
                elif evento.key == pygame.K_DOWN:
                    nova_linha += 1
                elif evento.key == pygame.K_LEFT:
                    nova_coluna -= 1
                elif evento.key == pygame.K_RIGHT:
                    nova_coluna += 1

                if posicao_valida(nova_linha, nova_coluna):
                    pos_jogador = [nova_linha, nova_coluna]
                    if base.LABIRINTO[nova_linha][nova_coluna] == 2:
                        vitoria = True

        tela.fill(COR_FUNDO)
        desenhar_labirinto(tela)
        desenhar_jogador(tela, pos_jogador)
        pygame.display.flip()

        if vitoria:
            escolha = tela_vitoria()

            if escolha == "proxima":
                # carrega a próxima fase
                carregar_fase(base.fase_atual + 1)
                pos_jogador = base.encontrar_inicio()
                vitoria = False
            else:  # "sair"
                rodando = False

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
