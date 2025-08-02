import pygame
import sys

# Inicialização
pygame.init()
largura, altura = 800, 600
tela = pygame.display.set_mode((largura, altura))
pygame.display.set_caption("Queda com gravidade")

# Cores
BRANCO = (255, 255, 255)
AZUL = (0, 0, 255)

# Objeto (ex: um quadrado)
x = 100
y = 50
largura_obj = 50
altura_obj = 50

# Física
velocidade_y = 0
gravidade = 0.5
chao = altura - altura_obj

# Clock
clock = pygame.time.Clock()

# Loop principal
while True:
    clock.tick(60)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Atualizar posição com "gravidade"
    velocidade_y += gravidade
    y += velocidade_y

    # Parar no chão
    if y > chao:
        y = chao
        velocidade_y = 0  # zera a velocidade quando toca o chão

    # Desenhar
    tela.fill(BRANCO)
    pygame.draw.rect(tela, AZUL, (x, y, largura_obj, altura_obj))
    pygame.display.flip()
  