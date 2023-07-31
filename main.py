import pygame
import random
import sys

pygame.init()

# akna seadistus
x_ekraan = 800
y_ekraan = 600
ekraan = pygame.display.set_mode([x_ekraan, y_ekraan])
pygame.display.set_caption("Ping Pong | Gerten Pilv'")
suund_x = 2 if random.randint(0, 1) == 0.1 else -0.1
suund_y = 1 if random.randint(0, 1) == 0.1 else -0.1
pall_x = 420
pall_y = 300
char1_skoor_lugeja = 0
char2_skoor_lugeja = 0
def mäng():
    # tausta tegemine :p
    def taust():
        punkt = 15
        rect_laius = 20
        x_punkt = x_ekraan // 2 + rect_laius // 2
        ekraan.fill([0, 0, 0])
        for i in range(y_ekraan):
            if punkt == 0:
                pygame.draw.rect(ekraan, [255, 255, 255], [x_punkt, i, 20, 70], 0)
                punkt = 100
            punkt -= 1

    # mängija 1
    v1x = 0
    mängija1x = 30
    mängija1y = 100
    def char1(mängija1x, mängija1y):
        pygame.draw.rect(ekraan, [255, 255, 255], [mängija1x, mängija1y, 12, 70], 0)
        pygame.draw.rect(ekraan, [173, 173, 173], [mängija1x, mängija1y - 2, 14, 74], 3)

    # mängija 2
    v2x = 0
    mängija2x = 45
    mängija2y = 100
    def char2(mängija2x, mängija2y):
        pygame.draw.rect(ekraan, [255, 255, 255], [x_ekraan - mängija2x, mängija2y, 12, 70], 0)
        pygame.draw.rect(ekraan, [173, 173, 173], [x_ekraan - mängija2x, mängija2y - 2, 14, 74], 3)

    # pall
    def pall():
        global pall_y, pall_x, suund_y, suund_x, char2_skoor_lugeja, char1_skoor_lugeja
        pygame.draw.circle(ekraan, [255, 255, 255], [pall_x, pall_y], 12, 0)
        pygame.draw.circle(ekraan, [173, 173, 173], [pall_x, pall_y], 13, 3)
        if pall_y <= 0 or pall_y >= y_ekraan:
            suund_y *= -1
        elif int(pall_x) == int(mängija1x) + 12 and int(pall_y) in range(int(mängija1y) - 10, int(mängija1y) + 70):
            suund_x *= -1
        elif int(pall_x) == int(x_ekraan - mängija2x) and int(pall_y) in range(int(mängija2y) - 10, int(mängija2y) + 70):
            suund_x *= -1
        if pall_x <= 20:
            suund_x = 2 if random.randint(0, 1) == 0.1 else -0.1
            suund_y = 1 if random.randint(0, 1) == 0.1 else -0.1
            pall_x = 420
            pall_y = 300
            char2_skoor_lugeja += 1
        elif pall_x >= 770:
            suund_x = 2 if random.randint(0, 1) == 0 else -0.1
            suund_y = 1 if random.randint(0, 1) == 0 else -0.1
            pall_x = 420
            pall_y = 300
            char1_skoor_lugeja += 1
        pall_x += suund_x
        pall_y += suund_y
        print("see on x:", pall_x)
        print("see on y:", pall_y)

    def char1_skoor(skoor):
        font = pygame.font.Font('font.ttf', 70)
        tekst_pildina = font.render(str(skoor), 1, [255, 255, 255])
        ekraan.blit(tekst_pildina, [350, 20])

    def char2_skoor(skoor):
        font = pygame.font.Font('font.ttf', 70)
        tekst_pildina = font.render(str(skoor), 1, [255, 255, 255])
        ekraan.blit(tekst_pildina, [470, 20])

    while True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()
            elif i.type == pygame.KEYDOWN:
                if i.key == pygame.K_w:
                    v1x = -0.5
                elif i.key == pygame.K_s:
                    v1x = 0.5
                elif i.key == pygame.K_UP:
                    v2x = -0.5
                elif i.key == pygame.K_DOWN:
                    v2x = 0.5
            elif i.type == pygame.KEYUP:
                if i.key == pygame.K_w or i.key == pygame.K_s:
                    v1x = 0
                if i.key == pygame.K_UP or i.key == pygame.K_DOWN:
                    v2x = 0
        mängija1y += v1x
        mängija2y += v2x
        taust()
        char1_skoor(char1_skoor_lugeja)
        char2_skoor(char1_skoor_lugeja)
        pall()
        char1(mängija1x, mängija1y)
        char2(mängija2x, mängija2y)
        pygame.display.flip()

def tiitel():
    def pealkiri(x, y):
        font = pygame.font.Font('font.ttf', 150)
        tekst_pildina = font.render("PING-PONG", 1, [255, 255, 255])
        ekraan.blit(tekst_pildina, [x, y])

    def autor(x, y):
        font = pygame.font.Font('font.ttf', 50)
        tekst_pildina = font.render("Made by: Gerten Pilv", 1, [255, 255, 0])
        ekraan.blit(tekst_pildina, [x, y])

    def start_nupp(x, y, värv):
        font = pygame.font.Font('font.ttf', 130)
        if värv == True:
            color = [255, 255, 0]
        else:
            color = [255, 255, 255]
        tekst_pildina = font.render("START", 1, color)
        ekraan.blit(tekst_pildina, [x, y])

    def about_nupp(x, y, värv):
        font = pygame.font.Font('font.ttf', 130)
        if värv == True:
            color = [255, 255, 0]
        else:
            color = [255, 255, 255]
        tekst_pildina = font.render("ABOUT", 1, color)
        ekraan.blit(tekst_pildina, [x, y])

    taust = pygame.image.load("taust.png")
    while True:
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                sys.exit()
            if i.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if pos[0] in range(270, 506) and pos[1] in range(247, 335):
                    mäng()

        ekraan.blit(taust, (5, 5))
        pealkiri(165, 55)
        autor(225, 165)
        #START NUPP
        if pygame.mouse.get_pos()[0] in range(270, 506) and pygame.mouse.get_pos()[1] in range(247, 335):
            start_nupp(270, 247, True)
        else:
            start_nupp(270, 247, False)
        #ABOUT nupp
        if pygame.mouse.get_pos()[0] in range(270, 506) and pygame.mouse.get_pos()[1] in range(350, 436):
            about_nupp(270, 350, True)
        else:
            about_nupp(270, 350, False)
        print(pygame.mouse.get_pos())
        pygame.display.flip()

tiitel()
pygame.quit()
