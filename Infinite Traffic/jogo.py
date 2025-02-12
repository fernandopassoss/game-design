import pygame
pygame.init()

x = 500
y = 450

posicao_x = 375
posicao_y = 450


velocidade = 20
velocidade_outros = 30

fundo = pygame.image.load('imagens/background.jpg')

carro = pygame.image.load('imagens/carro_principal.png')
carro = pygame.transform.scale(carro, (165, 350))

carro1 = pygame.image.load('imagens/carro1.png')
carro1 = pygame.transform.scale(carro1, (165, 350))

carro2 = pygame.image.load('imagens/carro2.png')
carro2 = pygame.transform.scale(carro2, (165, 350))

carro4 = pygame.image.load('imagens/carro4.png')
carro4 = pygame.transform.scale(carro4, (165, 350))

carro5 = pygame.image.load('imagens/carro5.png')
carro5 = pygame.transform.scale(carro5, (165, 350))

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

janela = pygame.display.set_mode((900, 1000))
pygame.display.set_caption("INFINITE TRAFFIC")

janela_aberta = True

while janela_aberta:
    pygame.time.delay(50)

    # Verificação de eventos ()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    # Movimentação do círculo (continua enquanto a tecla for pressionada)
    comandos = pygame.key.get_pressed()

    if comandos[pygame.K_UP]:
        y -= velocidade

    if comandos[pygame.K_DOWN]:
        y += velocidade

    if comandos[pygame.K_LEFT]:
        x -= velocidade

    if comandos[pygame.K_RIGHT]:
        x += velocidade
    
    if posicao_y <= -350:
        posicao_y = 1000

    posicao_y -= velocidade_outros

    # Atualiza a janela
    janela.blit(fundo, (0,0))
    janela.blit(carro, (x,y))

    janela.blit(carro1, (posicao_x, posicao_y))
    janela.blit(carro2, (posicao_x - 300, posicao_y))
    janela.blit(carro4, (posicao_x + 300, posicao_y))

    pygame.display.update()

pygame.quit()
