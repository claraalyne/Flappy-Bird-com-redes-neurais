import pygame
import os

class Peixe:
    imagem_peixe = pygame.image.load(os.path.join("imagens", "Sardinha.png"))
    largura_original, altura_original = imagem_peixe.get_size()
    IMAGEM_PEIXE = pygame.transform.scale(
    imagem_peixe,
    (largura_original // 1.4, altura_original // 1.4))

    def __init__(self, y):
        self.velocidade = 0
        self.y = y
        self.altura = self.y
        self.tempo = 0
        self.aceleracao = .5

    def pularpeixe(self):

        self.velocidade = -10.5
        self.tempo = 0 
        self.altura = self.y

    def moverpeixe(self):

        self.velocidade += self.aceleracao
        self.y += self.velocidade

        if self.y + self.altura_original//1.4 >= 602:
            self.y = 602 - self.altura_original//1.4
            self.velocidade = 0
                
        if self.y - self.altura_original//4 - 16 < 0:
            self.y = 0 + self.altura_original//4 + 16
            self.velocidade = 0 
        
    def desenhar(self, tela):
        tela.blit(self.IMAGEM_PEIXE, (204,self.y))

class BarraDentro:
    imagem_original = pygame.image.load(os.path.join("imagens", "barra_certa.jpeg"))
    largura_original, altura_original = imagem_original.get_size()
    IMAGEM_BARRA = pygame.transform.scale(
    imagem_original,
    (largura_original // 4, altura_original // 5.0)
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

    def mover(self):

        self.velocidade += self.aceleracao
        self.y += self.velocidade

        if self.y + self.altura_original//5.0 >= 602:
            self.y = 602 - self.altura_original//5.0 
            self.velocidade = 0
            
        if self.y - self.altura_original//4 - 16 < 0:
            self.y = 0 + self.altura_original//4 + 16
            self.velocidade = 0
    
    def desenhar(self, tela):
        tela.blit(self.IMAGEM_BARRA, (204,self.y))
    
    

class BarraFora:
    pass