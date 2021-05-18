# ===== Inicialização =====
#Import
import pygame as pg
import random
import time
#Init
pg.init()
#Tela principal
WIDTH = 800
HEIGHT = 800
window = pg.display.set_mode ((WIDTH,HEIGHT))
pg.display.set_caption("Metal Slug Remake")

#Assets
assets={} #Dicionario Assets Jogo
startsc_anim=[] #Lista Animações tela inicial
for i in range (2):
    #Arquivos para animação - 0 a 1
    nome_arquivo = "/Users/antonioamaralegydiomartins/OneDrive - Insper - Institudo de Ensino e Pesquisa/DesSoft/Pygame/Jogo_da_hora/Tela Inicial/TIS{}.png".format(i)
    img = pg.image.load(nome_arquivo).convert()
    img = pg.transform.scale (img,(0,0))
    startsc_anim.append(img)
assets["startsc_anim"]=startsc_anim
#estrutura de dados
game = True
start_screen = True
# == Start Screen ==
while start_screen:
    for event in pg.event.get():
        #Carregando imagem
        startsc=pg.image.load("/Users/antonioamaralegydiomartins/OneDrive - Insper - Institudo de Ensino e Pesquisa/DesSoft/Pygame/Jogo_da_hora/Tela Inicial/TIS.png")
        #Direcionando imagem
        window.blit(startsc,(0,0))
        #Aperte Enter para começar / Quebrar Looping
        if event.type== pg.KEYDOWN: #Detecta Evento de Apertar
            if event.key == pg.K_RETURN:
                start_screen=False
        pg.display.update()
# ===== Game Loop =====
while game:
    #Trata Eventos
    for event in pg.event.get():
        if event.type == pg.QUIT:
            game = False
    #Saidas
    window.fill((255,255,255))
    #Update
    pg.display.update()

#===== Finalização =====
pg.quit()
