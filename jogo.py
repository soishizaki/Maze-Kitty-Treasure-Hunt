import pygame
import sys
import base
from base import *
import random

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
TEMPO_FASE = 31  # segundos por fase
FONT_TEMPO = pygame.font.SysFont("Arial", 15, bold=True)

# === imagens ===
IMG_INICIO = pygame.image.load("img/inicio.png").convert()
IMG_INICIO = pygame.transform.smoothscale(IMG_INICIO, (LARGURA_TELA, ALTURA_TELA))

IMG_PROXIMA = pygame.image.load("img/proxima_fase.png").convert()
IMG_PROXIMA = pygame.transform.smoothscale(IMG_PROXIMA, (LARGURA_TELA, ALTURA_TELA))

IMG_FINAL = pygame.image.load("img/fim.png").convert()
IMG_FINAL = pygame.transform.smoothscale(IMG_FINAL, (LARGURA_TELA, ALTURA_TELA))

# Tela de instruções (infos)
# Telas de instruções (infos)
# ajuste os nomes se seus arquivos tiverem outro nome
IMG_INFO1 = pygame.image.load("img/infos1.png").convert()   # tela das setas + Next
IMG_INFO1 = pygame.transform.smoothscale(IMG_INFO1, (LARGURA_TELA, ALTURA_TELA))

IMG_INFO2 = pygame.image.load("img/infos2.png").convert()   # tela do tempo + Back
IMG_INFO2 = pygame.transform.smoothscale(IMG_INFO2, (LARGURA_TELA, ALTURA_TELA))


# --- Telas de informações (Instructions, 2 páginas) ---
def tela_infos():
    # botão no canto inferior direito (mesmo lugar nas duas imagens)
    botao_rect = pygame.Rect(LARGURA_TELA - 170, ALTURA_TELA - 80, 142, 60)

    pagina = 1  # começa na página 1 (setas)

    while True:
        # desenha a página atual
        if pagina == 1:
            tela.blit(IMG_INFO1, (0, 0))
        else:
            tela.blit(IMG_INFO2, (0, 0))

        # DEBUG: pra ver a área clicável, descomenta:
        # pygame.draw.rect(tela, (0, 255, 0), botao_rect, 2)

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if evento.type == pygame.KEYDOWN:
                # ESC fecha o jogo
                if evento.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

                # Enter / Espaço:
                # - na página 1 -> Next (vai pra página 2)
                # - na página 2 -> Back (volta pro menu)
                if evento.key in (pygame.K_RETURN, pygame.K_SPACE):
                    SOM_BOTAO.play()
                    if pagina == 1:
                        pagina = 2
                    else:
                        return  # volta pro menu

                # Backspace também funciona como "Back" na página 2
                if pagina == 2 and evento.key == pygame.K_BACKSPACE:
                    SOM_BOTAO.play()
                    return

            if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if botao_rect.collidepoint(evento.pos):
                    SOM_BOTAO.play()
                    if pagina == 1:
                        # Next -> página 2
                        pagina = 2
                    else:
                        # Back -> volta pro menu inicial
                        return

        pygame.display.flip()
        clock.tick(60)


# --- Tela de menu inicial ---
def menu_inicial():
    botao_play = pygame.Rect(
        LARGURA_TELA // 2 - 130, 
        ALTURA_TELA - 120,        
        260,                      
        60                        
    )

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

# Cores possíveis para as estrelinhas
CORES_ESTRELAS = [
    (255, 255, 0),   # amarelo
    (255, 192, 203), # rosa
    (135, 206, 250), # azul claro
    (144, 238, 144), # verde claro
    (255, 165, 0),   # laranja
    (255, 255, 255)  # branco
]

def criar_estrela(multicolor=False):
    """Cria uma estrelinha começando acima da tela."""
    cor = random.choice(CORES_ESTRELAS) if multicolor else (255, 255, 0)
    return {
        "x": random.randint(0, LARGURA_TELA),
        "y": random.randint(-ALTURA_TELA, 0),
        "vel": random.uniform(1.5, 4.0),
        "raio": random.randint(2, 4),
        "cor": cor
    }

# --- Tela de próxima fase ---
def tela_proxima_fase():
    botao_next = pygame.Rect(
        LARGURA_TELA // 2 - 200,
        ALTURA_TELA - 180,
        400,
        100
    )

    # cria várias estrelinhas iniciais
    estrelas = [criar_estrela() for _ in range(300)]
    rodando = True

    while rodando:
        clock.tick(60)

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

        # atualiza posição das estrelinhas
        for e in estrelas:
            e["y"] += e["vel"]
            # quando passa da parte de baixo, recria lá em cima
            if e["y"] > ALTURA_TELA + 10:
                novo = criar_estrela()
                e["x"] = novo["x"]
                e["y"] = novo["y"]
                e["vel"] = novo["vel"]
                e["raio"] = novo["raio"]

        # desenha o fundo da tela de próxima fase
        tela.blit(IMG_PROXIMA, (0, 0))

        # desenha as estrelinhas por cima
        for e in estrelas:
            pygame.draw.circle(
                tela,
                (255, 255, 0),                      # amarelo estrela
                (int(e["x"]), int(e["y"])),
                e["raio"]
            )

        # (sem hover, só o botão mesmo – se quiser voltar com hover dá pra somar depois)

        pygame.display.flip()


# --- Tela de final/restart ---
def tela_final():
    botao_play = pygame.Rect(
        LARGURA_TELA // 2 - 205,
        ALTURA_TELA - 180,
        410,
        95
    )

    # estrelinhas COLORIDAS na tela de vitória
    estrelas = [criar_estrela(multicolor=True) for _ in range(500)]

    while True:
        clock.tick(60)

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

        # atualiza estrelas
        for e in estrelas:
            e["y"] += e["vel"]
            if e["y"] > ALTURA_TELA + 10:
                novo = criar_estrela(multicolor=True)
                e["x"], e["y"], e["vel"], e["raio"], e["cor"] = \
                    novo["x"], novo["y"], novo["vel"], novo["raio"], novo["cor"]

        # desenha o fundo de vitória
        tela.blit(IMG_FINAL, (0, 0))

        # desenha estrelas por cima
        for e in estrelas:
            pygame.draw.circle(
                tela,
                e["cor"],
                (int(e["x"]), int(e["y"])),
                e["raio"]
            )

        pygame.display.flip()

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
        texto_tempo = FONT_TEMPO.render(f"Timer: {tempo_restante:02d} seconds", True, COR_TEXTO)
        tela.blit(texto_tempo, (15, 5))

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
