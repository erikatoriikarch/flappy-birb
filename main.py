import random, pygame, sys
from pygame.locals import *
from birb import Birb
from fork import Fork
from score import Scorebar
from coin import Coin

pygame.init()
screen_info = pygame.display.Info()

size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (0,0,0)
background = pygame.image.load('background.jpg')
background = pygame.transform.scale(background, (width, height))

coins = pygame.sprite.Group()
scorebars = pygame.sprite.Group()
forks = pygame.sprite.Group()
startPos = (width/8, height/2)
player = Birb(startPos)
gapsize = 200
loopCount = 0
score = 0

def lose():
    font = pygame.font.SysFont(None, 70)
    text = font.render("You got eaten D:", True, (255, 255, 255, ))
    text_rect = text.get_rect()
    text_rect.center = width / 2, height / 2

    while True:
        clock.tick(60)
        screen.fill(color)
        screen.blit(text, text_rect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    forks.empty()
                    Player.reset(startPos)
                    return
def losefall():
    font = pygame.font.SysFont(None, 70)
    text = font.render("You were squashed by gravity D:", True, (255, 255, 255,))
    text_rect = text.get_rect()
    text_rect.center = width / 2, height / 2

    while True:
        clock.tick(60)
        screen.fill(color)
        screen.blit(text, text_rect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    forks.empty()
                    Player.reset(startPos)
                    return

def main():
    global Ticks, loopCount, score
    num = 70
    while True:
        clock.tick(60)
        if loopCount % 70 == 35:
                coins.add(Coin((int(screen_info.current_w), random.randint(0, int(screen_info.current_h)))))
        if loopCount % 70 == 0:
            toppos = random.randint(0, height/2) - 400
            forks.add(Fork((width -100, toppos + gapsize + 650)))
            forks.add(Fork((width -100, toppos), True))
            scorebars.add(Scorebar((width-100, 0)))

        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    player.speed[1] = -10

        screen.fill(color)
        player.update()
        forks.update()
        scorebars.update()
        coins.update()
        gets_coins = pygame.sprite.spritecollide(player, coins, False)
        gets_score = pygame.sprite.spritecollide(player, scorebars, False)
        gets_hit = pygame.sprite.spritecollide(player, forks, False)
        gets_hit2 = player.rect.center[1] > height
        screen.blit(background, [0, 0])
        forks.draw(screen)
        scorebars.draw(screen)
        coins.draw(screen)
        screen.blit(player.image, player.rect)

        font = pygame.font.SysFont(None, 70)
        text = font.render("Score: " + str(score), True, (0, 0, 0,))
        text_rect = text.get_rect()
        text_rect.center = width / 2, height / 2
        screen.blit(text, text_rect)

        pygame.display.flip()
        if num > 1:
            num -=0.00001
        loopCount += 1

        if gets_coins:
            score+=10
            coins.remove(gets_coins)

        if gets_score:
            score+=1
            scorebars.remove(gets_score)
        
        if gets_hit:
            lose()
            break

        if gets_hit2:
            losefall()
            break


if __name__ == "__main__":
    main()