import os
os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % (425, 35) # Makes window pop up in specific spot

import pygame, sys
pygame.init()

from random import *

def combat(player, enemy):
# Loads in screen GUI for game
    screen = pygame.display.set_mode((1000, 1000))

    # loading all sprites
    FLOORTILE = pygame.image.load("Magiclash_Floor_1.png")
    MENU_TILE = pygame.image.load("Magiclash_Combat_menu.png")
    MENU_TILE_SMALL = pygame.image.load("Magiclash_Combat_menu.png")
    MENU_TILE_SMALL = pygame.transform.scale(MENU_TILE_SMALL, (30,30))

    WIZARD = pygame.image.load("Magiclash_Wizard_Battle.png")
    WIZARD = pygame.transform.scale(WIZARD, (200, 200))

    ENEMY = enemy.image
    ENEMY = pygame.transform.scale(ENEMY, (200,200))

    BUTTON = pygame.image.load("Magiclash_Button.png")


    HEALTH_TEXT = pygame.image.load("Magiclash_HP_Text.png")
    HEALTH_TEXT = pygame.transform.scale(HEALTH_TEXT, (50, 50))


    MANA_TEXT = pygame.image.load("Magiclash_AP_Text.png")
    MANA_TEXT = pygame.transform.scale(MANA_TEXT, (50, 50))

    LEVEL_TEXT = pygame.image.load("Magiclash_Lv_Icon.png")

    MAGIC_MISSLE_PIC = pygame.image.load("Magiclash_Magic_Missle.png")
    FIREBOLT_PIC = pygame.image.load("Magiclash_Firebolt.png")
    MP_SAP_PIC = pygame.image.load("Magiclash_MP_Sap.png")
    HEAL_PIC = pygame.image.load("Magiclash_Heal.png")
    ICE_SHARD_PIC = pygame.image.load("Magiclash_Ice_Shard.png")
    RIP = pygame.image.load("Magiclash_Dead.png")


    # loading combat space tiles
    for i in range(100, 900, 100):
        for j in range(100, 500, 100):
            screen.blit(FLOORTILE, (i, j))
            pygame.display.update()

    # loading wizard to combat zone
    screen.blit(WIZARD, (200,200))

    # loading enemy to combat zone (Changed y from 100 -> 200)
    screen.blit(ENEMY, (700,200))

    # loading combat menu tiles
    for i in range(100, 900, 100):
        for j in range(600, 900, 100):
            screen.blit(MENU_TILE, (i, j))
            pygame.display.update()

    # loading health text
    screen.blit(HEALTH_TEXT, (115, 825))
    pygame.display.update()

    # loading mana text
    screen.blit(MANA_TEXT, (540, 825))
    pygame.display.update()

    # loading level text
    screen.blit(LEVEL_TEXT, (740,820))
    pygame.display.update()

    class Spell(object):
        def __init__(self, name, atk, mp):
            self.name = name
            self.atk = atk
            self.MP = mp


    # spells
    MAGIC_MISSLE = Spell("Magic Missle", 3, 2)
    FIREBOLT = Spell("Firebolt", randint(4,6), 4)
    ICE_SHARD = Spell("Ice Shard", 3, 7)
    HEAL = Spell("Heal", 5 * player.level, 3)
    MP_SAP = Spell("Mana Sap", 3 * player.level, 0)

    # Loading Combat Button
    for i in range(250, 850, 200):
        for j in range(610, 810, 100):
            screen.blit(BUTTON, (i, j))
            pygame.display.update()
    screen.blit(MP_SAP_PIC, (270, 610))
    screen.blit(MAGIC_MISSLE_PIC, (470, 610))
    screen.blit(FIREBOLT_PIC, (670, 610))
    screen.blit(HEAL_PIC, (270, 710))
    screen.blit(ICE_SHARD_PIC, (470, 710))
    screen.blit(RIP, (670, 710))
    #screen.blit()

    def text_objects(text, font):
        textSurface = font.render(text, True, (255, 255, 255))
        return textSurface, textSurface.get_rect()


    def message_display(text):

        largeText = pygame.font.Font('freesansbold.ttf', 12)
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = (500, 550)
        pygame.draw.rect(screen, (0, 0, 0), [300, 500, 600, 100])
        screen.blit(TextSurf, TextRect)
        pygame.display.update()

    def text_objects_HP(text, font):
        textSurface = font.render(text, True, (255, 255, 255))
        return textSurface, textSurface.get_rect()


    def message_display_HP(player):

        text = str(player.HP)
        largeText = pygame.font.Font('freesansbold.ttf', 14)
        TextSurf, TextRect = text_objects_HP(text, largeText)
        TextRect.center = (185, 845)
        pygame.draw.rect(screen, (0, 0, 0), [165, 825, 40, 40])
        screen.blit(TextSurf, TextRect)
        pygame.display.update()

    def text_objects_MP(text, font):
        textSurface = font.render(text, True, (255, 255, 255))
        return textSurface, textSurface.get_rect()


    def message_display_MP(player):

        text = str(player.MP)
        largeText = pygame.font.Font('freesansbold.ttf', 14)
        TextSurf, TextRect = text_objects_MP(text, largeText)
        TextRect.center = (610, 845)
        pygame.draw.rect(screen, (0, 0, 0), [590, 825, 40, 40])
        screen.blit(TextSurf, TextRect)
        pygame.display.update()

    def text_objects_LVL(text, font):
        textSurface = font.render(text, True, (255, 255, 255))
        return textSurface, textSurface.get_rect()


    def message_display_LVL(player):

        text = str(player.level)
        largeText = pygame.font.Font('freesansbold.ttf', 14)
        TextSurf, TextRect = text_objects_LVL(text, largeText)
        TextRect.center = (830, 845)
        pygame.draw.rect(screen, (0, 0, 0), [800, 825, 60, 40])
        screen.blit(TextSurf, TextRect)
        pygame.display.update()


    def enemy_attack(player, enemy):
        atkNum = randint(1, 3)

        if enemy.name == "Slime":
            if atkNum == 1:
                message_display("The slime lunges at you")
                pygame.time.wait(2000)
                dmg = 2
                player.HP = player.HP - dmg
            elif atkNum == 2:
                message_display("The slime spits a barrage of goo at you")
                pygame.time.wait(2000)
                hit = randint(1, 3)
                dmg = hit
                message_display("You're hit " + str(hit) + " time(s)")
                pygame.time.wait(2000)
                player.HP = player.HP - dmg
            else:
                message_display("The slime absorbs nutrients from the air")
                pygame.time.wait(2000)
                enemy.HP = enemy.HP + 1
                if enemy.HP > enemy.maxHP:
                    enemy.HP = enemy.maxHP
        elif enemy.name == "Skeleton":
            if atkNum == 1:
                message_display("The skeleton throws a bone at you")
                pygame.time.wait(2000)
                dmg = 3
                player.HP = player.HP - dmg
            elif atkNum == 2:
                message_display("The skeleton attempts to charge into you...")
                pygame.time.wait(2000)
                if randint(1, 3) > 1:
                    message_display("but it misses and takes 2 damage")
                    pygame.time.wait(2000)
                    enemy.HP = enemy.HP - 2
                else:
                    dmg = 4
                    message_display("and rams you into the ground!")
                    pygame.time.wait(2000)
                    player.HP = player.HP - dmg
            else:
                message_display("The skeleton shakes...menacingly")
                pygame.time.wait(2000)
        elif enemy.name == "Zombie":
            if atkNum == 1:
                message_display("The zombie bites into your arm, damaging you and healing itself")
                pygame.time.wait(2000)
                dmg = 3
                player.HP = player.HP - dmg
                enemy.HP = enemy.HP + 2
                if enemy.HP > enemy.maxHP:
                    enemy.HP = enemy.maxHP
            elif atkNum == 2:
                message_display("The zombie slashes at you")
                pygame.time.wait(2000)
                dmg = 4
                player.HP = player.HP - dmg
            else:
                message_display("The zombie pulls out a brain and starts chowing down on it")
                pygame.time.wait(2000)
                enemy.HP = enemy.HP + 3
                if enemy.HP > enemy.maxHP:
                    enemy.HP = enemy.maxHP
        elif enemy.name == "Imp":
            if atkNum == 1:
                message_display("The imp casts a lesser fire spell on you")
                pygame.time.wait(2000)
                dmg = 7
                player.HP = player.HP - dmg
            elif atkNum == 2:
                message_display("The imp barrages you with flaming spears")
                pygame.time.wait(2000)
                hit = randint(1, 4)
                dmg = hit * 4
                message_display("You're hit " + str(hit) + " time(s)")
                pygame.time.wait(2000)
                player.HP = player.HP - dmg
            else:
                message_display("The imp snickers at you")
                pygame.time.wait(2000)
                dmg = 0
        elif enemy.name == "Wizardling":
            if atkNum == 1:
                message_display("The wizardling surrounds you in a dark orb filled with dark energy")
                pygame.time.wait(2500)
                hit = randint(2, 7)
                dmg = hit * 2
                message_display("You're hit " + str(hit) + " times")
                pygame.time.wait(2000)
                player.HP = player.HP - dmg
            elif atkNum == 2:
                message_display("The wizardling fires a magic missle at you")
                pygame.time.wait(2000)
                dmg = 8
                player.HP = player.HP - dmg
            elif atkNum == 3:
                message_display("The wizardling tries to heal itself..")
                pygame.time.wait(2000)
                if randint(1, 4) == 1:
                    message_display("And healed itself to full!")
                    pygame.time.wait(2000)
                    enemy.HP = enemy.maxHP
                else:
                    message_display("But it fails")
                    pygame.time.wait(2000)
                    dmg = 0

        message_display("It's your turn")
        pygame.time.wait(2000)

    class Arrow(object):
        def __init__(self):
            self.image = pygame.image.load("Magiclash_Arrow.png")
            # Position
            self.x = 200
            self.y = 625
        #Menu Key Operations
        def menu_keys(self, surface):  # Movement is restricted to the size of the map via the and checks
            key = pygame.key.get_pressed()
            dist = 200  # Every press of a movement key will move the player 1 'tile'
            if key[pygame.K_DOWN] and not (self.y + dist - 100 > 725):  # down key
                surface.blit(MENU_TILE_SMALL, (self.x, self.y))
                self.y += dist -100
                pygame.display.update()
            elif key[pygame.K_UP] and not (self.y - dist + 100 < 625):  # up key
                surface.blit(MENU_TILE_SMALL, (self.x, self.y))
                self.y -= dist - 100
                pygame.display.update()
            if key[pygame.K_RIGHT] and not (self.x + dist > 600):  # right key
                surface.blit(MENU_TILE_SMALL, (self.x, self.y))
                self.x += dist
                pygame.display.update()
            elif key[pygame.K_LEFT] and not (self.x - dist < 200):  # left key
                surface.blit(MENU_TILE_SMALL, (self.x, self.y))
                self.x -= dist
                pygame.display.update()

        def draw(self, surface):
            # Displays the player at the current position
            surface.blit(self.image, (self.x, self.y))
            pygame.display.update()

    # MUSIC/Sound LOAD
    pygame.mixer.music.load("Battle.mp3")
    pygame.mixer.music.play(-1)
    # Core of game
    arrow = Arrow()
    arrow.draw(screen)

    while True:

        turn = 1 # 1 Means it's the players turn, 2 means It's the enemies turn
        for event in pygame.event.get():
            key = pygame.key.get_pressed()
            if event.type == pygame.QUIT:
                sys.exit()
            message_display_HP(player)
            message_display_MP(player)
            message_display_LVL(player)
            if turn == 1:
                key = pygame.key.get_pressed()
                if key[pygame.K_f]:
                    if arrow.x == 200 and arrow.y == 625:
                        message_display("Spell MP sap used.")
                        pygame.time.wait(2000)
                        if not player.maxMP < player.MP + MP_SAP.atk:
                            player.MP += MP_SAP.atk
                        else:
                            player.MP = player.maxMP
                        turn = 2
                    if arrow.x == 400 and arrow.y == 625:
                        if player.MP >= MAGIC_MISSLE.MP:
                            message_display("Spell magic missle used.")
                            pygame.time.wait(2000)
                            enemy.HP -= MAGIC_MISSLE.atk
                            player.MP -= MAGIC_MISSLE.MP
                            turn = 2
                        else:
                            message_display("You don't have enough MANA.")
                            pygame.time.wait(2000)
                    if arrow.x == 600 and arrow.y == 625:
                        if player.level >= 2:
                            if player.MP >= FIREBOLT.MP:
                                message_display("Spell Firebolt used.")
                                pygame.time.wait(2000)
                                enemy.HP -= FIREBOLT.atk
                                player.MP -= FIREBOLT.MP
                                turn = 2
                            else:
                                message_display("You don't have enough MANA.")
                                pygame.time.wait(2000)
                        else:
                            message_display("You muse be level 2 to use this spell")
                            pygame.time.wait(2000)
                    if arrow.x == 200 and arrow.y == 725:
                        if player.level >= 3:
                            if player.MP >= HEAL.MP:
                                message_display("Spell heal used.")
                                pygame.time.wait(2000)
                                if not player.maxHP < player.HP + HEAL.atk:
                                    player.HP += HEAL.atk
                                    message_display_HP(player)
                                    player.MP -= HEAL.MP
                                else:
                                    player.HP = player.maxHP
                                    pygame.time.wait(2000)
                                turn = 2
                            else:
                                message_display("You don't have enough MANA.")
                                pygame.time.wait(2000)
                        else:
                            message_display("You must be level 3 to use this spell")
                            pygame.time.wait(2000)
                    if arrow.x == 400 and arrow.y == 725:
                        if player.level >= 4:
                            if player.MP >= ICE_SHARD.MP:
                                message_display("Spell Ice Shard used.")
                                pygame.time.wait(1500)
                                hit = randint(1,5)
                                message_display("It hit " + str(hit) + " time(s)")
                                pygame.time.wait(1500)
                                enemy.HP -= ICE_SHARD.atk * hit
                                player.MP -= ICE_SHARD.MP
                                turn = 2
                            else:
                                message_display("You don't have enough MANA.")
                                pygame.time.wait(1500)
                        else:
                            message_display("You must be level 4 to use this spell")
                            pygame.time.wait(1500)
                    if arrow.x == 600 and arrow.y == 725:
                        if player.level >= 5:
                            message_display("Spell RIP used.")
                            pygame.time.wait(1500)
                            enemy.HP = enemy.HP - 100
                            turn = 2
                        else:
                            message_display("You muse be level 5 to use this spell")
                            pygame.time.wait(1500)

                message_display_HP(player)
                message_display_MP(player)
            arrow.menu_keys(screen)
            arrow.draw(screen)


        if enemy.HP <= 0:
            message_display("YOU WON, PRESS ANY KEY TO CONTINUE")
            enemy.defeated = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    player.EXP += enemy.EXP
                    player.level_up()

                    player.HP += 3 * player.level
                    player.MP += 3 * player.level
                    if player.HP > player.maxHP:
                        player.HP = player.maxHP
                    if player.MP > player.maxMP:
                        player.MP = player.maxMP

                    return

        elif turn == 2:
            message_display("It's the enemy's turn")
            pygame.time.wait(2000)
            enemy_attack(player, enemy)

        if player.HP <= 0:
            message_display("YOU DIED, PRESS ANY KEY TO QUIT")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    sys.exit()

def victory(player):
    # Loads in screen GUI for game
    screen = pygame.display.set_mode((1000, 1000))

    # loading all sprites
    FLOORTILE = pygame.image.load("Magiclash_Floor_1.png")
    MENU_TILE = pygame.image.load("Magiclash_Combat_menu.png")
    MENU_TILE_SMALL = pygame.image.load("Magiclash_Combat_menu.png")
    MENU_TILE_SMALL = pygame.transform.scale(MENU_TILE_SMALL, (30, 30))


    WIZARD = pygame.image.load("Magiclash_Wizard_Battle.png")
    WIZARD = pygame.transform.scale(WIZARD, (200, 200))

    ENEMY = pygame.image.load("Magiclash_#1_Wizard_Template.png")
    ENEMY = pygame.transform.scale(ENEMY, (200, 200))

    BUTTON = pygame.image.load("Magiclash_Button.png")

    HEALTH_TEXT = pygame.image.load("Magiclash_HP_Text.png")
    HEALTH_TEXT = pygame.transform.scale(HEALTH_TEXT, (50, 50))

    MANA_TEXT = pygame.image.load("Magiclash_AP_Text.png")
    MANA_TEXT = pygame.transform.scale(MANA_TEXT, (50, 50))

    LEVEL_TEXT = pygame.image.load("Magiclash_Lv_Icon.png")

    MAGIC_MISSLE_PIC = pygame.image.load("Magiclash_Magic_Missle.png")
    FIREBOLT_PIC = pygame.image.load("Magiclash_Firebolt.png")
    MP_SAP_PIC = pygame.image.load("Magiclash_MP_Sap.png")
    HEAL_PIC = pygame.image.load("Magiclash_Heal.png")
    ICE_SHARD_PIC = pygame.image.load("Magiclash_Ice_Shard.png")
    RIP = pygame.image.load("Magiclash_Dead.png")

    # loading combat space tiles
    for i in range(100, 900, 100):
        for j in range(100, 500, 100):
            screen.blit(FLOORTILE, (i, j))
            pygame.display.update()

    # loading wizard to combat zone
    screen.blit(WIZARD, (200, 200))

    # loading enemy to combat zone (Changed y from 100 -> 200)
    screen.blit(ENEMY, (700, 200))

    # loading combat menu tiles
    for i in range(100, 900, 100):
        for j in range(600, 900, 100):
            screen.blit(MENU_TILE, (i, j))
            pygame.display.update()

    # loading health text
    screen.blit(HEALTH_TEXT, (115, 825))
    pygame.display.update()

    # loading mana text
    screen.blit(MANA_TEXT, (540, 825))
    pygame.display.update()

    # loading level text
    screen.blit(LEVEL_TEXT, (740, 820))
    pygame.display.update()

    # Loading Combat Button
    for i in range(250, 850, 200):
        for j in range(610, 810, 100):
            screen.blit(BUTTON, (i, j))
            pygame.display.update()
    screen.blit(MP_SAP_PIC, (270, 610))
    screen.blit(MAGIC_MISSLE_PIC, (470, 610))
    screen.blit(FIREBOLT_PIC, (670, 610))
    screen.blit(HEAL_PIC, (270, 710))
    screen.blit(ICE_SHARD_PIC, (470, 710))
    screen.blit(RIP, (670, 710))

    def text_objects(text, font):
        textSurface = font.render(text, True, (255, 255, 255))
        return textSurface, textSurface.get_rect()


    def message_display(text):

        largeText = pygame.font.Font('freesansbold.ttf', 12)
        TextSurf, TextRect = text_objects(text, largeText)
        TextRect.center = (500, 550)
        pygame.draw.rect(screen, (0, 0, 0), [300, 500, 600, 100])
        screen.blit(TextSurf, TextRect)
        pygame.display.update()

    def text_objects_HP(text, font):
        textSurface = font.render(text, True, (255, 255, 255))
        return textSurface, textSurface.get_rect()

    def message_display_HP(player):

        text = str(player.HP)
        largeText = pygame.font.Font('freesansbold.ttf', 14)
        TextSurf, TextRect = text_objects_HP(text, largeText)
        TextRect.center = (185, 845)
        pygame.draw.rect(screen, (0, 0, 0), [165, 825, 40, 40])
        screen.blit(TextSurf, TextRect)
        pygame.display.update()

    def text_objects_MP(text, font):
        textSurface = font.render(text, True, (255, 255, 255))
        return textSurface, textSurface.get_rect()

    def message_display_MP(player):

        text = str(player.MP)
        largeText = pygame.font.Font('freesansbold.ttf', 14)
        TextSurf, TextRect = text_objects_MP(text, largeText)
        TextRect.center = (610, 845)
        pygame.draw.rect(screen, (0, 0, 0), [590, 825, 40, 40])
        screen.blit(TextSurf, TextRect)
        pygame.display.update()

    def text_objects_LVL(text, font):
        textSurface = font.render(text, True, (255, 255, 255))
        return textSurface, textSurface.get_rect()

    def message_display_LVL(player):

        text = str(player.level)
        largeText = pygame.font.Font('freesansbold.ttf', 14)
        TextSurf, TextRect = text_objects_LVL(text, largeText)
        TextRect.center = (830, 845)
        pygame.draw.rect(screen, (0, 0, 0), [800, 825, 60, 40])
        screen.blit(TextSurf, TextRect)
        pygame.display.update()

    message_display_HP(player)
    message_display_MP(player)
    message_display_LVL(player)

    message_display("Oh hi! I'm the #1 Wizard in all the realm")
    pygame.time.wait(3000)
    message_display("I already defeated the evil wizard, so uh...")
    pygame.time.wait(3000)
    message_display("I guess you can go home! Lucky you getting off work early! :)")
    pygame.time.wait(3000)

    message_display("YOU WON!! Press any key to quit")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                sys.exit()


FLOORTILE = pygame.image.load("Magiclash_Floor_1.png")

class FLOOR(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.image.load("Magiclash_Floor_1.png")
        self.rect = pygame.Rect(self.x, self.y, 100, 100)

    def draw(self, surface):
        # Displays the player at the current position
        surface.blit(self.image, (self.x, self.y))


class BLOCK(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.image.load("Magiclash_Floor_Block.png")
        self.rect = pygame.Rect(self.x, self.y, 100, 100)

    def draw(self, surface):
        # Displays the player at the current position
        surface.blit(self.image, (self.x, self.y))


class STAIRS(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.image.load("Magiclash_Stairs.png")
        self.rect = pygame.Rect(self.x, self.y, 100, 100)

    def draw(self, surface):
        # Displays the player at the current position
        surface.blit(self.image, (self.x, self.y))


# Declaring Floors
FLOOR1 = [[0 for x in range(8)] for y in range(8)]
FLOOR2 = [[0 for x in range(8)] for y in range(8)]
FLOOR3 = [[0 for x in range(8)] for y in range(8)]
FLOOR4 = [[0 for x in range(8)] for y in range(8)]
FLOOR5 = [[0 for x in range(8)] for y in range(8)]
FLOOR6 = [[0 for x in range(8)] for y in range(8)]

# Filling walls with fake walls
WALLS1 = [[0 for x in range(8)] for y in range(8)]
WALLS2 = [[0 for x in range(8)] for y in range(8)]
WALLS3 = [[0 for x in range(8)] for y in range(8)]
WALLS4 = [[0 for x in range(8)] for y in range(8)]
WALLS5 = [[0 for x in range(8)] for y in range(8)]
WALLS6 = [[0 for x in range(8)] for y in range(8)]

for i in range(0, 8):
    for j in range(0, 8):
        WALLS1[i][j] = BLOCK(0, 0)
        WALLS2[i][j] = BLOCK(0, 0)
        WALLS3[i][j] = BLOCK(0, 0)
        WALLS4[i][j] = BLOCK(0, 0)
        WALLS5[i][j] = BLOCK(0, 0)
        WALLS6[i][j] = BLOCK(0, 0)

# FILLING FLOOR 1
for i in range(0, 8):  # Displaying basic floor map
    for j in range(0, 8):
        FLOOR1[j][i] = FLOOR((j * 100) + 100, (i * 100) + 100)
FLOOR1[5][0] = STAIRS(600, 100)
STAIRLOCATION1 = STAIRS(600,100)
FLOOR1[1][1] = BLOCK(200, 200)
WALLS1[1][1] = BLOCK(200, 200)
for i in range(2, 4):
    for j in range(4, 7):
        FLOOR1[j][i] = BLOCK((j * 100) + 100, (i * 100) + 100)
        WALLS1[j][i] = BLOCK((j * 100) + 100, (i * 100) + 100)
for i in range(3, 5):
    FLOOR1[0][i] = BLOCK(100, (i * 100) + 100)
    WALLS1[0][i] = BLOCK(100, (i * 100) + 100)
for i in range(4, 8):
    FLOOR1[2][i] = BLOCK(300, (i * 100) + 100)
    WALLS1[2][i] = BLOCK(300, (i * 100) + 100)
for j in range(5,8):
    FLOOR1[j][6] = BLOCK((j * 100) + 100, 700)
    WALLS1[j][6] = BLOCK((j * 100) + 100, 700)

# FILLING FLOOR 2
for i in range(0, 8):  # Displaying basic floor map
    for j in range(0, 8):
        FLOOR2[j][i] = FLOOR((j * 100) + 100, (i * 100) + 100)
FLOOR2[2][7] = STAIRS(300,800)
STAIRLOCATION2 = STAIRS(300,800)
for i in range(0,2):
    for j in range(0,8):
        FLOOR2[i][j] = BLOCK((i * 100) + 100, (j*100) + 100)
        WALLS2[i][j] = BLOCK((i * 100) + 100, (j*100) + 100)
for i in range(6,8):
    for j in range(0,8):
        FLOOR2[i][j] = BLOCK((i * 100) + 100, (j*100) + 100)
        WALLS2[i][j] = BLOCK((i * 100) + 100, (j*100) + 100)
WALLS2[6][0] = BLOCK(700, 100)

# FILLING FLOOR 3
for i in range(0, 8):  # Displaying basic floor map
    for j in range(0, 8):
        FLOOR3[j][i] = FLOOR((j * 100) + 100, (i * 100) + 100)
FLOOR3[7][3] = STAIRS(800,400)
STAIRLOCATION3 = STAIRS(800,400)
for j in range(0,2):
    FLOOR3[0][j] = BLOCK(100, (j * 100) + 100)
    WALLS3[0][j] = BLOCK(100, (j * 100) + 100)
    FLOOR3[4][j] = BLOCK(500, (j * 100) + 100)
    WALLS3[4][j] = BLOCK(500, (j * 100) + 100)
for j in range(6,8):
    FLOOR3[0][j] = BLOCK(100, (j * 100) + 100)
    WALLS3[0][j] = BLOCK(100, (j * 100) + 100)
    FLOOR3[4][j] = BLOCK(500, (j * 100) + 100)
    WALLS3[4][j] = BLOCK(500, (j * 100) + 100)
for i in range(1,4,2):
    FLOOR3[i][2] = BLOCK((i * 100) + 100, 300)
    WALLS3[i][2] = BLOCK((i * 100) + 100, 300)
    FLOOR3[i][5] = BLOCK((i * 100) + 100, 600)
    WALLS3[i][5] = BLOCK((i * 100) + 100, 600)
for i in range(6,8):
    FLOOR3[i][1] = BLOCK((i * 100) + 100, 200)
    WALLS3[i][1] = BLOCK((i * 100) + 100, 200)
    FLOOR3[i][5] = BLOCK((i * 100) + 100, 600)
    WALLS3[i][5] = BLOCK((i * 100) + 100, 600)
for j in range(2,5,2):
    FLOOR3[5][j] = BLOCK(600, (j * 100) + 100)
    WALLS3[5][j] = BLOCK(600, (j * 100) + 100)

# FILLING FLOOR 4
for i in range(0, 8):  # Displaying basic floor map
    for j in range(0, 8):
        FLOOR4[j][i] = FLOOR((j * 100) + 100, (i * 100) + 100)
FLOOR4[0][3] = STAIRS(100, 400)
STAIRLOCATION4 = STAIRS(100, 400)

for i in range(0, 8):
    for j in range(0, 3):
        FLOOR4[i][j] = BLOCK((i * 100) + 100, (j * 100) + 100)
        WALLS4[i][j] = BLOCK((i * 100) + 100, (j * 100) + 100)
for i in range(0,8):
    for j in range(4,8):
        FLOOR4[i][j] = BLOCK((i * 100) + 100, (j * 100) + 100)
        WALLS4[i][j] = BLOCK((i * 100) + 100, (j * 100) + 100)

# FILLING FLOOR 5
for i in range(0, 8):  # Displaying basic floor map
    for j in range(0, 8):
        FLOOR5[j][i] = FLOOR((j * 100) + 100, (i * 100) + 100)

for i in range(0, 8):
    FLOOR5[i][0] = BLOCK((i * 100) + 100, 100)
    WALLS5[i][0] = BLOCK((i * 100) + 100, 100)
    FLOOR5[i][7] = BLOCK((i * 100) + 100, 800)
    WALLS5[i][7] = BLOCK((i * 100) + 100, 800)

for i in range(0, 8, 7):
    FLOOR5[i][1] = BLOCK((i * 100) + 100, 200)
    WALLS5[i][1] = BLOCK((i * 100) + 100, 200)
    FLOOR5[i][2] = BLOCK((i * 100) + 100, 300)
    WALLS5[i][2] = BLOCK((i * 100) + 100, 300)
    FLOOR5[i][4] = BLOCK((i * 100) + 100, 500)
    WALLS5[i][4] = BLOCK((i * 100) + 100, 500)
    FLOOR5[i][5] = BLOCK((i * 100) + 100, 600)
    WALLS5[i][5] = BLOCK((i * 100) + 100, 600)
    FLOOR5[i][6] = BLOCK((i * 100) + 100, 700)
    WALLS5[i][6] = BLOCK((i * 100) + 100, 700)
FLOOR5[7][3] = STAIRS(800, 400)
STAIRLOCATION5 = STAIRS(800, 400)
for j in range(2, 6):
    FLOOR5[2][j] = BLOCK(300, (j * 100) + 100)
    WALLS5[2][j] = BLOCK(300, (j * 100) + 100)
    FLOOR5[5][j] = BLOCK(600, (j * 100) + 100)
    WALLS5[5][j] = BLOCK(600, (j * 100) + 100)
for i in range(3, 5):
    for j in range(3, 5):
        FLOOR5[i][j] = BLOCK((i * 100) + 100, (j * 100) + 100)
        WALLS5[i][j] = BLOCK((i * 100) + 100, (j * 100) + 100)

# FILLING FLOOR 6
for i in range(0, 8):  # Displaying basic floor map
    for j in range(0, 8):
        FLOOR6[j][i] = FLOOR((j * 100) + 100, (i * 100) + 100)
WALLS6[4][3] = BLOCK(500, 400)

# Printing the floor
def floor_print(floor, surface):
    for i in range(0,8):
        for j in range(0,8):
            floor[i][j].draw(surface)
            pygame.display.update()

# Class for enemies
class Mob(pygame.sprite.Sprite):
    def __init__(self, name, hp, exp, atk, spriteImg, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.name = name
        self.HP = hp
        self.maxHP = hp
        self.EXP = exp
        self.atk = atk

        self.x = x
        self.y = y
        self.image = pygame.image.load(spriteImg)
        self.rect = pygame.Rect(self.x, self.y, 100, 100)

        self.defeated = False

    def draw(self, surface):
        # Displays the enemy at the current position
        surface.blit(self.image, (self.x, self.y))

# The main character the user controls
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        # Sprite
        self.image = pygame.image.load("Magiclash_Wizard_Idle.png")
        # Position
        self.x = 100
        self.y = 800
        self.rect = pygame.Rect(self.x, self.y, 100, 100)
        # Extra Info
        self.HP = 10
        self.maxHP = 10
        self.MP = 10
        self.maxMP = 10
        self.EXP = 0
        self.level = 1
        self.spells = []

    # Movement is restricted to the size of the map via the and checks
    def handle_keys(self, surface, walls):
        key = pygame.key.get_pressed()
        dist = 100  # Every press of a movement key will move the player 1 'tile'
        if key[pygame.K_DOWN] and not(self.y + dist > 800):  # down key
            self.y += dist
            self.rect = pygame.Rect(self.x, self.y, 100, 100)
            if not(self.check_collision(walls)):
                surface.blit(FLOORTILE, (self.x, self.y - dist))
            else:
                self.y -= dist
                self.rect = pygame.Rect(self.x, self.y, 100, 100)
        elif key[pygame.K_UP] and not(self.y - dist < 100):  # up key
            self.y -= dist
            self.rect = pygame.Rect(self.x, self.y, 100, 100)
            if not(self.check_collision(walls)):
                surface.blit(FLOORTILE, (self.x, self.y + dist))
            else:
                self.y += dist
                self.rect = pygame.Rect(self.x, self.y, 100, 100)
        if key[pygame.K_RIGHT] and not(self.x + dist > 800):  # right key
            self.x += dist
            self.rect = pygame.Rect(self.x, self.y, 100, 100)
            if not(self.check_collision(walls)):
                surface.blit(FLOORTILE, (self.x - dist, self.y))
            else:
                self.x -= dist
                self.rect = pygame.Rect(self.x, self.y, 100, 100)
        elif key[pygame.K_LEFT] and not(self.x - dist < 100):  # left key
            self.x -= dist
            self.rect = pygame.Rect(self.x, self.y, 100, 100)
            if not(self.check_collision(walls)):
                surface.blit(FLOORTILE, (self.x + dist, self.y))
            else:
                self.x += dist
                self.rect = pygame.Rect(self.x, self.y, 100, 100)

    def draw(self, surface):
        # Displays the player at the current position
        surface.blit(self.image, (self.x, self.y))

    # Checkes if where user wants to move will make them collide with a wall
    def check_collision(self, walls):
        for wallRow in walls:
            for wall in wallRow:
                if player.rect.colliderect(wall.rect):
                    return True
        return False

    # Checks if the user is standing on a stair tile
    def check_stairs(self,stairs):
        if player.rect.colliderect(stairs.rect):
            return True
        return False

    # Checks if the player should level up after combat
    def level_up(self):
        if self.EXP < 45: # Lv 1
            self.level = 1
            self.maxHP = 10
            self.maxMP = 10
        elif self.EXP >= 45 and self.EXP < 100 and self.level == 1: # Lv 2
            self.level = 2
            self.maxHP = 20
            self.maxMP = 15
            self.HP = self.maxHP
            self.MP = self.maxMP
        elif self.EXP >= 100 and self.EXP < 250 and self.level == 2: # Lv 3
            self.level = 3
            self.maxHP = 30
            self.maxMP = 20
            self.HP = self.maxHP
            self.MP = self.maxMP
        elif self.EXP >= 250 and self.EXP < 500 and self.level == 3: # Lv 4
            self.level = 4
            self.maxHP = 40
            self.maxMP = 25
            self.HP = self.maxHP
            self.MP = self.maxMP
        elif self.EXP > 500 and self.level == 4: # Lv 5
            self.level = 5
            self.maxHP = 50
            self.maxMP = 30
            self.HP = self.maxHP
            self.MP = self.maxMP


# Loading and setting basic variables
screen = pygame.display.set_mode((1000, 1000))  # Loads in screen GUI for game
player = Player() # Creates Player Object
pygame.display.set_caption("Magiclash")  # Names caption of window

# Setting Allowed events
pygame.event.set_blocked(pygame.MOUSEMOTION)  # Disable all event to start

# TESTING MUSIC
pygame.mixer.music.load("Wizard's Tower.mp3") # Loads Music
pygame.mixer.music.play(-1)

currentFloor = 1
printedFloor = False

# Declaring all enemies
slime_F1_1 = Mob("Slime", 5, 10, 11, "Magiclash_Slime.png", 200, 500)
slime_F1_2 = Mob("Slime", 5, 10, 2, "Magiclash_Slime.png", 700, 500)
skeleton_F1_1 = Mob("Skeleton", 10, 25, 4, "Magiclash_Skeleton.png", 600, 800)

skeleton_F2_1 = Mob("Skeleton", 10, 25, 4, "Magiclash_Skeleton.png", 400, 600)
skeleton_F2_2 = Mob("Skeleton", 10, 25, 4, "Magiclash_Skeleton.png", 400, 300)

zombie_F3_1 = Mob("Zombie", 10, 50, 3, "Magiclash_Zombie.png", 300, 600)
zombie_F3_2 = Mob("Zombie", 10, 50, 3, "Magiclash_Zombie.png", 600, 400)

skeleton_F4_1 = Mob("Skeleton", 10, 25, 4, "Magiclash_Skeleton.png", 500, 400)
skeleton_F4_2 = Mob("Skeleton", 10, 25, 4, "Magiclash_Skeleton.png", 300, 400)
imp_F4_1 = Mob("Imp", 10, 75, 8, "Magiclash_Imp.png", 400, 400)

wizardling_F5_1 = Mob("Wizardling", 25, 100, 7, "Magiclash_Wizardling.png", 300, 200)
wizardling_F5_2 = Mob("Wizardling", 25, 100, 7, "Magiclash_Wizardling.png", 300, 700)
wizardling_F5_3 = Mob("Wizardling", 25, 100, 7, "Magiclash_Wizardling.png", 600, 200)
wizardling_F5_4 = Mob("Wizardling", 25, 100, 7, "Magiclash_Wizardling.png", 600, 700)

number1_F6 = Mob("#1 Wizard", 1000, 1000, 1000, "Magiclash_#1_Wizard_Template.png", 400, 400)

while True:  # Core of game
    if currentFloor == 1 and not printedFloor:  # Prints Floor 1

        floor_print(FLOOR1, screen)
        player.draw(screen)
        if not slime_F1_1.defeated:
            slime_F1_1.draw(screen)
        if not slime_F1_2.defeated:
            slime_F1_2.draw(screen)
        if not skeleton_F1_1.defeated:
            skeleton_F1_1.draw(screen)
        pygame.display.update()
        printedFloor = True

    elif currentFloor == 2 and not printedFloor:  # Prints Floor 2

        floor_print(FLOOR2, screen)
        player.draw(screen)
        if not skeleton_F2_1.defeated:
            skeleton_F2_1.draw(screen)
        if not skeleton_F2_2.defeated:
            skeleton_F2_2.draw(screen)
        pygame.display.update()
        printedFloor = True

    elif currentFloor == 3 and not printedFloor:  # Prints Floor 3

        floor_print(FLOOR3, screen)
        player.draw(screen)
        if not zombie_F3_1.defeated:
            zombie_F3_1.draw(screen)
        if not zombie_F3_2.defeated:
            zombie_F3_2.draw(screen)
        pygame.display.update()
        printedFloor = True

    elif currentFloor == 4 and not printedFloor:  # Prints Floor 4

        floor_print(FLOOR4, screen)
        player.draw(screen)
        if not skeleton_F4_1.defeated:
            skeleton_F4_1.draw(screen)
        if not skeleton_F4_2.defeated:
            skeleton_F4_2.draw(screen)
        if not imp_F4_1.defeated:
            imp_F4_1.draw(screen)
        pygame.display.update()
        printedFloor = True

    elif currentFloor == 5 and not printedFloor:  # Prints Floor 5

        floor_print(FLOOR5, screen)
        player.draw(screen)
        if not wizardling_F5_1.defeated:
            wizardling_F5_1.draw(screen)
        if not wizardling_F5_2.defeated:
            wizardling_F5_2.draw(screen)
        if not wizardling_F5_3.defeated:
            wizardling_F5_3.draw(screen)
        if not wizardling_F5_4.defeated:
            wizardling_F5_4.draw(screen)
        pygame.display.update()
        printedFloor = True

    elif currentFloor == 6 and not printedFloor:  # Prints Floor 6

        floor_print(FLOOR6, screen)
        player.draw(screen)
        number1_F6.draw(screen)
        screen.blit(pygame.image.load("Magiclash_Grave.png"), (500, 400))

        pygame.display.update()
        printedFloor = True

    if currentFloor == 1:  # Works on Floor 1
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if player.rect.colliderect(slime_F1_1.rect) and not slime_F1_1.defeated:
                combat(player, slime_F1_1)
                printedFloor = False

                pygame.mixer.music.load("Wizard's Tower.mp3")  # Loads Music
                pygame.mixer.music.play(-1)

            elif player.rect.colliderect(slime_F1_2.rect) and not slime_F1_2.defeated:
                combat(player, slime_F1_2)
                printedFloor = False

                pygame.mixer.music.load("Wizard's Tower.mp3")  # Loads Music
                pygame.mixer.music.play(-1)

            elif player.rect.colliderect(skeleton_F1_1.rect) and not skeleton_F1_1.defeated:
                combat(player, skeleton_F1_1)
                printedFloor = False

                pygame.mixer.music.load("Wizard's Tower.mp3")  # Loads Music
                pygame.mixer.music.play(-1)

            if player.check_stairs(STAIRLOCATION1):
                currentFloor = 2
                printedFloor = False

            player.handle_keys(screen, WALLS1)
            player.draw(screen)
            pygame.display.update()

    elif currentFloor == 2: # Works on Floor 2
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if player.rect.colliderect(skeleton_F2_1.rect) and not skeleton_F2_1.defeated:
                combat(player, skeleton_F2_1)
                printedFloor = False
            elif player.rect.colliderect(skeleton_F2_2.rect) and not skeleton_F2_2.defeated:
                combat(player, skeleton_F2_2)
                printedFloor = False

                pygame.mixer.music.load("Wizard's Tower.mp3")  # Loads Music
                pygame.mixer.music.play(-1)

            # Find way to interact with #1 Wizard

            if player.check_stairs(STAIRLOCATION2):
                currentFloor = 3
                printedFloor = False

            player.handle_keys(screen, WALLS2)
            player.draw(screen)
            pygame.display.update()

    elif currentFloor == 3:  # Works on Floor 3
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if player.rect.colliderect(zombie_F3_1.rect) and not zombie_F3_1.defeated:
                combat(player, zombie_F3_1)
                printedFloor = False

                pygame.mixer.music.load("Wizard's Tower.mp3")  # Loads Music
                pygame.mixer.music.play(-1)

            elif player.rect.colliderect(zombie_F3_2.rect) and not zombie_F3_2.defeated:
                combat(player, zombie_F3_2)
                printedFloor = False

                pygame.mixer.music.load("Wizard's Tower.mp3")  # Loads Music
                pygame.mixer.music.play(-1)

            if player.check_stairs(STAIRLOCATION3):
                currentFloor = 4
                printedFloor = False

            player.handle_keys(screen, WALLS3)
            player.draw(screen)
            pygame.display.update()

    elif currentFloor == 4:  # Works on Floor 4
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if player.rect.colliderect(skeleton_F4_1.rect) and not skeleton_F4_1.defeated:
                combat(player, skeleton_F4_1)
                printedFloor = False

                pygame.mixer.music.load("Wizard's Tower.mp3")  # Loads Music
                pygame.mixer.music.play(-1)

            elif player.rect.colliderect(skeleton_F4_2.rect) and not skeleton_F4_2.defeated:
                combat(player, skeleton_F4_2)
                printedFloor = False

                pygame.mixer.music.load("Wizard's Tower.mp3")  # Loads Music
                pygame.mixer.music.play(-1)

            elif player.rect.colliderect(imp_F4_1.rect) and not imp_F4_1.defeated:
                combat(player, imp_F4_1)
                printedFloor = False

                pygame.mixer.music.load("Wizard's Tower.mp3")  # Loads Music
                pygame.mixer.music.play(-1)

            if player.check_stairs(STAIRLOCATION4):
                currentFloor = 5
                printedFloor = False

            player.handle_keys(screen, WALLS4)
            player.draw(screen)
            pygame.display.update()

    elif currentFloor == 5:  # Works on Floor 5
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if player.rect.colliderect(wizardling_F5_1.rect) and not wizardling_F5_1.defeated:
                combat(player, wizardling_F5_1)
                printedFloor = False

                pygame.mixer.music.load("Wizard's Tower.mp3")  # Loads Music
                pygame.mixer.music.play(-1)

            elif player.rect.colliderect(wizardling_F5_2.rect) and not wizardling_F5_2.defeated:
                combat(player, wizardling_F5_2)
                printedFloor = False

                pygame.mixer.music.load("Wizard's Tower.mp3")  # Loads Music
                pygame.mixer.music.play(-1)

            elif player.rect.colliderect(wizardling_F5_3.rect) and not wizardling_F5_3.defeated:
                combat(player, wizardling_F5_3)
                printedFloor = False

                pygame.mixer.music.load("Wizard's Tower.mp3")  # Loads Music
                pygame.mixer.music.play(-1)

            elif player.rect.colliderect(wizardling_F5_4.rect) and not wizardling_F5_4.defeated:
                combat(player, wizardling_F5_4)
                printedFloor = False

                pygame.mixer.music.load("Wizard's Tower.mp3")  # Loads Music
                pygame.mixer.music.play(-1)

            if player.check_stairs(STAIRLOCATION5):
                currentFloor = 6
                printedFloor = False

            player.handle_keys(screen, WALLS5)
            player.draw(screen)
            pygame.display.update()

    elif currentFloor == 6:  # Works on Floor 5
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if player.rect.colliderect(number1_F6.rect):
                victory(player)
                sys.exit()

            player.handle_keys(screen, WALLS6)
            player.draw(screen)
            pygame.display.update()
