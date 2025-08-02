import pygame 
from pygame.locals import *
from sys import exit
import os
from classes import Peixe, BarraDentro

pygame.init()

largura = 500
altura = 800 #487
imagem_background = pygame.image.load(os.path.join("imagens","background.jpg"))


tela = pygame.display.set_mode((largura,altura))


pygame.display.set_caption('Pescaria')

pygame.font.init()
font_temporizador = pygame.font.SysFont('arial', 30)

barra = BarraDentro(480)
relogio = pygame.time.Clock()


while True:
    relogio.tick(60)

    for event in pygame.event.get():
        
        print(event)
        if event.type == QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    if keys[K_SPACE]:
        barra.pular()


    barra.mover()
    print(barra.y)
    tela.blit(imagem_background,(0,0))
    barra.desenhar(tela)

    pygame.display.update()

    