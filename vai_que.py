# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

pygame.init()

# ----- Gera tela principal
WIDTH = 1100
HEIGHT = 300
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Metal Slug da massa')


# ----- Inicia assets
image = pygame.image.load('Cenario/Montanha Clean 1100x300.png').convert()
image = pygame.transform.scale(image, (1100, 300))

# ----- Inicia estruturas de dados
game = True

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False

    # ----- Gera saídas
    window.fill((0, 0, 0))  # Preenche com a cor branca
    window.blit(image, (10, 10))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados


