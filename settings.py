class Settings():
    def __init__(self):
        # 界面宽
        self.screen_width = 1200

        # 界面长
        self.screen_height = 800

        # 底色
        self.bg_color = (230, 230, 230)

        # 飞船
        self.ship_limit = 3

        # 子弹
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 100

        # 外星人
        self.fleet_drop_speed = 10
        self.fleet_direction = 1  # 1右 -1左

        # 提高速度
        self.speedup_scale = 1.1
        # 提高点数
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    # 设置初始化
    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 20
        self.alien_speed_factor = 10
        self.bullet_speed_factor = 15
        self.fleet_direction = 1
        self.alien_points = 50

    # 加速
    def increase_speed(self):
        self.ship_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.bullet_speed_factor *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
