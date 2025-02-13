import pygame 
from random import randint
pygame.init()

x = 425  
y = 150

posicao_x = 425
posicao_y = 800
posicao_y_1 = 800
posicao_y_2 = 800
timer = 0
tempo_segundo = 0 

velocidade = 20
velocidade_outros = 30

fundo = pygame.image.load('imagens/background.png')

carro = pygame.image.load('imagens/carro_principal.png')
carro = pygame.transform.scale(carro, (165, 350))

carro1 = pygame.image.load('imagens/carro1.png')
carro1 = pygame.transform.scale(carro1, (165, 350))

carro2 = pygame.image.load('imagens/carro2.png')
carro2 = pygame.transform.scale(carro2, (165, 350))

carro4 = pygame.image.load('imagens/carro4.png')
carro4 = pygame.transform.scale(carro4, (165, 350))

carro5 = pygame.image.load('imagens/carro5.png')

carro6 = pygame.image.load('imagens/carro6.png')
carro6 = pygame.transform.scale(carro6, (165, 350))

carro7 = pygame.image.load('imagens/carro7.png')
carro7 = pygame.transform.scale(carro7, (165, 350))

carro8 = pygame.image.load('imagens/carro8.png')
carro8 = pygame.transform.scale(carro8, (165, 350))

carro9 = pygame.image.load('imagens/carro9.png')
carro9 = pygame.transform.scale(carro9, (165, 350))

carro10 = pygame.image.load('imagens/carro10.png')
carro10 = pygame.transform.scale(carro10, (165, 350))

font = pygame.font.SysFont('PressStart2P.ttf', 60)
janela = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("INFINITE TRAFFIC")

janela_aberta = True

while janela_aberta:
    pygame.time.delay(50)

    # Verificação de eventos ()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()

    if comandos[pygame.K_UP]:
        y -= velocidade

    if comandos[pygame.K_DOWN]:
        y += velocidade

    if comandos[pygame.K_LEFT] and x >= 95:
        x -= velocidade

    if comandos[pygame.K_RIGHT] and x <= 725:
        x += velocidade
    
    if (posicao_y <= -350) and (posicao_y_1 <= -350) and (posicao_y_2 <= -350):
        posicao_y = randint(800, 2000)
        posicao_y_1 = randint(800, 2000)
        posicao_y_2 = randint(800, 2000)

    if timer < 20:
        timer += 1
    else:
        tempo_segundo += 1
        timer = 0

    posicao_y -= velocidade_outros
    posicao_y_1 -= velocidade_outros + 2
    posicao_y_2 -= velocidade_outros + 10

    # Atualiza a janela
    janela.blit(fundo, (0, 0))
    janela.blit(carro, (x, y))
    janela.blit(carro1, (posicao_x, posicao_y))
    janela.blit(carro2, (posicao_x - 300, posicao_y_1))
    janela.blit(carro4, (posicao_x + 300, posicao_y_2))

    texto_sombra = font.render(f"Tempo: {tempo_segundo}", True, (20, 20, 20))
    texto = font.render(f"Tempo: {tempo_segundo}", True, (255, 200, 0))  

    pos_texto = texto.get_rect(center=(120, 50))
    janela.blit(texto_sombra, (pos_texto.x + 2, pos_texto.y + 2)) 
    janela.blit(texto, pos_texto)

    pygame.display.update()

pygame.quit()
