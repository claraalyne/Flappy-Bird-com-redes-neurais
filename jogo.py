import pygame 
from pygame.locals import *
from sys import exit
import os
from classes import Peixe, BarraDentro

pygame.init()

largura = 506
altura = 813 #487
imagem_background = pygame.image.load(os.path.join("imagens","background_certo.png"))
    #204, 156 -> 234, 156  
largura_original, altura_original = imagem_background.get_size()
imagem_background = pygame.transform.scale(imagem_background, (largura_original * 1.75, altura_original * 1.75))

tela = pygame.display.set_mode((largura,altura))


pygame.display.set_caption('Pescaria')

pygame.font.init()
font_temporizador = pygame.font.SysFont('arial', 30)

barra = BarraDentro(480)
peixe = Peixe(480)
relogio = pygame.time.Clock()


while True:
    relogio.tick(60)

    for event in pygame.event.get():
        
        print(event)
        if event.type == QUIT:
            pygame.quit()
            exit()

    keys = pygame.key.get_pressed()
    mouse = pygame.mouse.get_pressed()
    if keys[K_SPACE]:
        barra.pular()
    if mouse [0]:
         peixe.pularpeixe()


    peixe.moverpeixe()
    barra.mover()
    print(barra.y)
    tela.blit(imagem_background,(0,0))
    barra.desenhar(tela)
    peixe.desenhar(tela)

    pygame.display.update()

    