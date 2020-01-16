import pygame


class Ship():
    def __init__(self, screen, ai_settings):
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船外形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 初始位置在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # 移动
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        # 移动（速度、范围）
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx += self.ai_settings.ship_speed_factor
        elif self.moving_left and self.rect.left > self.screen_rect.left:
            self.rect.centerx -= self.ai_settings.ship_speed_factor
        elif self.moving_up:
            self.rect.bottom -= self.ai_settings.ship_speed_factor
        elif self.moving_down:
            self.rect.bottom += self.ai_settings.ship_speed_factor

        # self.rect.centerx = self.center

    def blitme(self):  # 指定位置画飞船
        self.screen.blit(self.image, self.rect)

    #重置飞船   //有问题
    def center_ship(self):
        self.center = self.screen_rect.centerx
        self.bottom = self.screen_rect.bottom