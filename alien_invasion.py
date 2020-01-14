import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group

def run_game():
    pygame.init()
    # screen = pygame.display.set_mode(1200,800)
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship = Ship(screen,ai_settings)
    alien = Alien(ai_settings,screen)
    bullets =  Group()

    while True:
        gf.check_events(ai_settings,screen,ship,bullets)
        ship.update()
        bullets.update()
        for bullet in bullets.copy():
            if bullet.rect.bottom <= 0:
                bullets.remove(bullet)
        # print(len(bullets))
        gf.update_screen(ai_settings,screen,ship,bullets)
        # for event in pygame.event .get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        # screen.fill(ai_settings.bg_color)
        # ship.blitme()
        # pygame.display.flip()

run_game()