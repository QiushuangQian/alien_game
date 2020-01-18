import sys
import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():
    pygame.init()
    # screen = pygame.display.set_mode(1200,800)
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    stats = GameStats(ai_settings)
    scoreboard = Scoreboard(ai_settings, screen, stats)

    # 创建飞船
    ship = Ship(screen, ai_settings)
    # 子弹编组
    bullets = Group()
    # 外星人编组
    aliens = Group()
    # 创建外星人群
    gf.create_fleet(ai_settings, screen, ship, aliens)
    # 按钮
    play_button = Button(ai_settings, screen, "Play")

    while True:
        gf.check_events(ai_settings, screen, stats, play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            gf.update_aliens(ai_settings, stats, screen, ship, aliens, bullets)
            gf.update_bullets(ai_settings, screen,stats,scoreboard, ship, aliens, bullets)
        gf.update_screen(ai_settings, screen, stats, scoreboard, ship, aliens, bullets, play_button)
        # bullets.update()
        # for bullet in bullets.copy():
        #     if bullet.rect.bottom <= 0:
        #         bullets.remove(bullet)
        # # print(len(bullets))

        # for event in pygame.event .get():
        #     if event.type == pygame.QUIT:
        #         sys.exit()
        # screen.fill(ai_settings.bg_color)
        # ship.blitme()
        # pygame.display.flip()


run_game()
