import pygame 
from random import randint
import emoji


def telaPerda(janela):
    pygame.draw.rect(janela, (0, 0, 0), pygame.Rect(250, 350, 500, 300))  
    font = pygame.font.SysFont('PressStart2P.ttf', 50)
    texto = font.render('Você perdeu uma Vida!', True, (255, 255, 255))
    gameOver = font.render('Game Over!', True, (255, 255, 255))
    if vidas == 2:
        emoji = pygame.image.load('imagens/duasVidas.png')  
        emoji = pygame.transform.scale(emoji, (250, 250))
    if vidas == 1:
        emoji = pygame.image.load('imagens/umaVida.png')  
        emoji = pygame.transform.scale(emoji, (250, 250))

    if vidas == 0:
        janela.blit(gameOver, (400,475))
        pygame.display.update()
        pygame.time.wait(2000)
        pygame.quit()

    janela.blit(texto, (300, 420)) 
    janela.blit(emoji, (375, 315))   
    pygame.display.update()
    pygame.time.wait(5000)
    
    


pygame.init()

vidas = 3
x = 425  
y = 150

posicao_x = 425
posicao_y = 1500
posicao_y_1 = 1200
posicao_y_2 = 1000
timer = 0
tempo_segundo = 0 

velocidade = 15
velocidade_outros = 15

fundo = pygame.image.load('imagens/background.png')

carro = pygame.image.load('imagens/carro_principal.png')
carro = pygame.transform.scale(carro, (165, 350))

carro1 = pygame.image.load('imagens/carro1.png')
carro1 = pygame.transform.scale(carro1, (165, 350))

carro2 = pygame.image.load('imagens/carro2.png')
carro2 = pygame.transform.scale(carro2, (165, 350))

carro4 = pygame.image.load('imagens/carro4.png')
carro4 = pygame.transform.scale(carro4, (165, 350))

font = pygame.font.SysFont('PressStart2P.ttf', 60)
janela = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("INFINITE TRAFFIC")

janela_aberta = True

while janela_aberta:
    pygame.time.delay(20)

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
    
 #verifica a colisao
    if (x < posicao_x + 165 and x + 165 > posicao_x )and( y < posicao_y + 350 and y + 350 > posicao_y):
        vidas = vidas - 1
        telaPerda(janela)
    
        posicao_y= randint(1200, 2000)

    if (x < posicao_x - 300 + 165 and x + 165 > posicao_x - 300 and 
    y < posicao_y_1 + 350 and y + 350 > posicao_y_1):
        y = 1200
        posicao_y= randint(1500, 2500)

    if (x < posicao_x + 300 + 165 and x + 165 > posicao_x + 300 and 
    y < posicao_y_2 + 350 and y + 350 > posicao_y_2):
        y = 1200
        posicao_y= randint(1700, 2700)




    if (posicao_y <= -180):
        pos_y = randint(800,1000)

    if (posicao_y_1 <= -180):
        posicao_y_1 = randint(1200, 2000)

    if (posicao_y_2 <= -180):
        posicao_y_2 = randint(2200, 3000)


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
