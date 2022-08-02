import pygame
from random import randint
def reset_game():
    pygame.init()


pygame.init()
x = 380 # maximo 530 minimo 230 meio 380
y = 100
pos_x = 526
pos_y = 1500
pos_y_a = 1000
pos_y_c = 1200
timer = 0
tempo_segundo = 0

velocidade = 15
velocidade_outros = 20

fundo = pygame.image.load('estrada.png')
carro = pygame.image.load('carro.png')
car1 = pygame.image.load('carro_purple.png')
car2 = pygame.image.load('carro_yellow.png')
car3 = pygame.image.load('carro_dark_red.png')

font = pygame.font.SysFont('arial black', 30)
texto = font.render("Tempo: ", True, (255,255,255), (0,0,0))
pos_texto = texto.get_rect()
pos_texto.center = (65, 50)

janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Criando um jogo com Python > By Rib@s")

janela_aberta = True
while janela_aberta:
    pygame.time.delay(70)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    comandos = pygame.key.get_pressed()
    #if comandos[pygame.K_UP]:
    #    y-= velocidade
    #if comandos[pygame.K_DOWN]:
    #    y+= velocidade
    if comandos[pygame.K_RIGHT] and x <= 530:
        x+= velocidade
    if comandos[pygame.K_LEFT] and x >= 230:
        x-= velocidade

    # detecta a colisão

    if ((x + 80 > pos_x and y + 180 > pos_y)): # colisão Lado direito
        reset_game()

    if ((x - 80 < pos_x -300 and y + 180 > pos_y_a)): # colisão lado esquerdo

        reset_game()

    if ((x + 80 > pos_x - 136 and y + 180 > pos_y_c)) and ((x - 80 < pos_x - 136 and y + 180 > pos_y_c )):

        reset_game()

    if (pos_y <= -80):
        pos_y = randint(800, 1000)
    if (pos_y_a <= -80):
        pos_y_a = randint(1300, 2000)
    if (pos_y_c <= -80):
        pos_y_c = randint(2300, 3000)

    if (timer <20):
        timer +=1
    else:
        tempo_segundo += 1
        texto = font.render("Tempo: "+str(tempo_segundo), True, (100,255,255), (0,0,0))
        timer = 0

    pos_y -= velocidade_outros
    pos_y_a -= velocidade_outros + 2
    pos_y_c -= velocidade_outros + 5

    janela.blit(fundo, (0,0))
    janela.blit(carro, (x, y))
    janela.blit(car1, (pos_x, pos_y))
    janela.blit(car2, (pos_x - 300, pos_y_a))
    janela.blit(car3, (pos_x - 136, pos_y_c))
    janela.blit(texto, pos_texto)


    pygame.display.update()

pygame.quit()