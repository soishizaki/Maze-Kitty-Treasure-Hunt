import pygame
import sys
import base
from base import *

pygame.init()
pygame.mixer.init()  # inicializa o áudio

# --- Música de fundo ---
pygame.mixer.music.load("sons/fundo.mp3")  # carrega a música de fundo
pygame.mixer.music.set_volume(0.4)         # volume da trilha (0.0 a 1.0)
pygame.mixer.music.play(-1)                # -1 = loop infinito

# --- Som de botão ---
SOM_BOTAO = pygame.mixer.Sound("sons/botao.mp3")
SOM_BOTAO.set_volume(0.8)  # volume do som de clique

# --- Config da tela ---
LARGURA_TELA = 600
ALTURA_TELA = 600
TITULO_JOGO = "Maze Kitty Treasure Hunt"
COR_FUNDO = (30, 30, 30)
COR_TEXTO = (255, 255, 255)

tela = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
pygame.display.set_caption(TITULO_JOGO)
clock = pygame.time.Clock()

# --- Fonte para o relógio ---
TEMPO_FASE = 45  # segundos por fase
FONT_TEMPO = pygame.font.SysFont("Arial", 32, bold=True)

# === imagens ===
IMG_INICIO = pygame.image.load("img/inicio.png").convert()
IMG_INICIO = pygame.transform.smoothscale(IMG_INICIO, (LARGURA_TELA, ALTURA_TELA))

IMG_PROXIMA = pygame.image.load("img/proxima_fase.png").convert()
IMG_PROXIMA = pygame.transform.smoothscale(IMG_PROXIMA, (LARGURA_TELA, ALTURA_TELA))

IMG_FINAL = pygame.image.load("img/fim.png").convert()
IMG_FINAL = pygame.transform.smoothscale(IMG_FINAL, (LARGURA_TELA, ALTURA_TELA))

# Tela de instruções (infos)
IMG_INFO = pygame.image.load("img/infos.png").convert()
IMG_INFO = pygame.transform.smoothscale(IMG_INFO, (LARGURA_TELA, ALTURA_TELA))


# --- Tela de informações (Instructions) ---
def tela_infos():
    # Botão BACK no canto inferior direito (para 600x600)
    botao_back = pygame.Rect(LARGURA_TELA - 170, ALTURA_TELA - 80, 142, 60)

    while True:
        tela.blit(IMG_INFO, (0, 0))

        # Se quiser ver a área clicável pra ajustar, descomente a linha abaixo:
        # pygame.draw.rect(tela, (0, 255, 0), botao_back, 2)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if evento.key in (pygame.K_RETURN, pygame.K_SPACE, pygame.K_BACKSPACE):
                    SOM_BOTAO.play()
                    return

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if botao_back.collidepoint(evento.pos):
                    SOM_BOTAO.play()
                    return  # volta ao menu

        pygame.display.flip()
        clock.tick(60)


# --- Tela de menu inicial ---
def menu_inicial():
    # Botão PLAY: centralizado mais perto da base
    botao_play = pygame.Rect(
        LARGURA_TELA // 2 - 130,  # centro - metade da largura (260/2)
        ALTURA_TELA - 120,        # bem perto da parte de baixo
        260,                      # largura
        60                        # altura
    )

    # Botão INFO: canto superior direito (posição segura em 600x600)
    botao_info = pygame.Rect(
        LARGURA_TELA - 115,  
        480,                
        70,                 
        70                 
    )

    while True:
        mouse_pos = pygame.mouse.get_pos()
        tela.blit(IMG_INICIO, (0, 0))

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                # ESC fecha o jogo
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                # Enter/Espaço = Play
                if evento.key in (pygame.K_RETURN, pygame.K_SPACE):
                    SOM_BOTAO.play()
                    return
                # tecla "i" abre a tela de infos
                if evento.key == pygame.K_i:
                    SOM_BOTAO.play()
                    tela_infos()

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                # clique no PLAY
                if botao_play.collidepoint(evento.pos):
                    SOM_BOTAO.play()
                    return
                # clique no INFO
                if botao_info.collidepoint(evento.pos):
                    SOM_BOTAO.play()
                    tela_infos()

        pygame.display.flip()
        clock.tick(60)



# --- Tela de próxima fase ---
def tela_proxima_fase():
    botao_next = pygame.Rect(LARGURA_TELA // 2 - 200,
                             ALTURA_TELA - 180,
                             400, 100)

    while True:
        mouse_pos = pygame.mouse.get_pos()
        tela.blit(IMG_PROXIMA, (0, 0))

        # hover
        if botao_next.collidepoint(mouse_pos):
            s = pygame.Surface((botao_next.width, botao_next.height), pygame.SRCALPHA)
            s.fill((255, 255, 255, 20))
            tela.blit(s, botao_next.topleft)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if evento.key in (pygame.K_RETURN, pygame.K_SPACE):
                    SOM_BOTAO.play()
                    return

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if botao_next.collidepoint(evento.pos):
                    SOM_BOTAO.play()
                    return

        pygame.display.flip()
        clock.tick(60)


# --- Tela de final/restart ---
def tela_final():
    botao_play = pygame.Rect(LARGURA_TELA // 2 - 205,
                             ALTURA_TELA - 180,
                             410, 95)

    while True:
        mouse_pos = pygame.mouse.get_pos()
        tela.blit(IMG_FINAL, (0, 0))

        # botão opaco com leve brilho no hover
        s = pygame.Surface((botao_play.width, botao_play.height), pygame.SRCALPHA)
        if botao_play.collidepoint(mouse_pos):
            s.fill((255, 255, 255, 40))  # brilho no hover
        else:
            s.fill((255, 255, 255, 15))  # leve opacidade padrão
        tela.blit(s, botao_play.topleft)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                if evento.key in (pygame.K_RETURN, pygame.K_SPACE):
                    SOM_BOTAO.play()
                    return "reiniciar"

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if botao_play.collidepoint(evento.pos):
                    SOM_BOTAO.play()
                    return "reiniciar"

        pygame.display.flip()
        clock.tick(60)


# --- Loop principal do jogo ---
def main():
    menu_inicial()  # mostra o menu antes de começar

    pos_jogador = base.encontrar_inicio()
    vitoria = False
    rodando = True

    # --- inicia o relógio da fase ---
    tempo_inicial = pygame.time.get_ticks()  # em milissegundos

    while rodando:
        clock.tick(30)

        # === EVENTOS ===
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

            if evento.type == pygame.KEYDOWN:
                # ESC fecha o jogo a partir da fase
                if evento.key == pygame.K_ESCAPE:
                    rodando = False
                if not vitoria:
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
                        if base.LABIRINTO[nova_linha][nova_coluna] in (2, 3, 4):
                            vitoria = True

        # === LÓGICA DO TEMPO ===
        segundos_decorridos = (pygame.time.get_ticks() - tempo_inicial) / 1000
        tempo_restante = max(0, int(TEMPO_FASE - segundos_decorridos))

        # se o tempo acabar e ainda não venceu: volta para a PRIMEIRA FASE
        if tempo_restante <= 0 and not vitoria:
            base.fase_atual = 0
            carregar_fase(0)
            pos_jogador = base.encontrar_inicio()
            vitoria = False
            tempo_inicial = pygame.time.get_ticks()  # zera o relógio
            continue

        # === DESENHO ===
        tela.fill(COR_FUNDO)
        desenhar_labirinto(tela)
        desenhar_jogador(tela, pos_jogador)

        # desenha o relógio no canto superior esquerdo
        texto_tempo = FONT_TEMPO.render(f"Tempo: {tempo_restante:02d}s", True, COR_TEXTO)
        tela.blit(texto_tempo, (20, 20))

        pygame.display.flip()

        # === TROCA DE FASE / FINAL ===
        if vitoria:
            if base.fase_atual < len(base.FASES) - 1:
                # mostra a tela "Next Level" antes de seguir
                tela_proxima_fase()
                carregar_fase(base.fase_atual + 1)
                pos_jogador = base.encontrar_inicio()
                vitoria = False
                tempo_inicial = pygame.time.get_ticks()
            else:
                escolha = tela_final()
                if escolha == "reiniciar":
                    carregar_fase(0)
                    base.fase_atual = 0
                    pos_jogador = base.encontrar_inicio()
                    vitoria = False
                    tempo_inicial = pygame.time.get_ticks()
                else:
                    rodando = False

    pygame.quit()
    sys.exit()


if __name__ == "__main__":
    main()
