import pygame
import os

class Peixe:
    #imgpeixe = imgpeixe
    def __init__(self, y):
        self.y = y
        self.velocidade = 0
        self.altura = self.y
    


class BarraDentro:
    imagem_original = pygame.image.load(os.path.join("imagens", "image.png"))
    largura_original, altura_original = imagem_original.get_size()
    IMAGEM_BARRA = pygame.transform.scale(
    imagem_original,
    (largura_original // 4, altura_original // 4)
)

    def __init__(self, y):
        self.y = y
        self.velocidade = 0
        self.altura = self.y
        self.tempo = 0
        self.aceleracao = .5

    def pular(self):
        self.velocidade = -10.5
        self.tempo = 0 
        self.altura = self.y
        print("PULOOOOOOOOOOOOU")

    def mover(self):

        if self.y > 800:
            self.y = 800
            self.velocidade = 0
            
        
        #self.tempo += 0.4
        #deslocamento = 0.5*(self.aceleracao)*(self.tempo**2) + self.velocidade * self.tempo
        #self.velocidade += self.aceleracao*self.tempo 
        #deslocamento = self.velocidade*self.tempo
        self.velocidade += self.aceleracao
        self.y += self.velocidade
        
        #if deslocamento > 16:
        #    deslocamento = 16
        #elif deslocamento < 0:
        #   deslocamento -= 2

        #self.y += deslocamento
    


    def desenhar(self, tela):
        tela.blit(self.IMAGEM_BARRA, (100,self.y))
    
    

class BarraFora:
    pass