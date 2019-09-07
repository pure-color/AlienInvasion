import pygame.font
from pygame.sprite import Group
from AlienInvasion.ship import Ship


class ScoreBoard():
    """显示得分信息的类"""

    def __init__(self, ai_settings, screen, stats):
        """初始化得分涉及的属性"""
        self.ai_settings = ai_settings
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.stats = stats

        # 显示得分信息时使用的字体属性
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 32)

        # 准备包含最高得分和当前得分图像
        self.perp_score()
        self.perp_high_score()
        self.perp_level()
        self.perp_ships()

    def perp_ships(self):
        """显示还余下多少飞船"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)

            ship.rect.x = self.ai_settings.screen_width - ship.rect.width
            ship.rect.y = self.ai_settings.screen_height - ship.rect.height - (
                    ship_number * ship.rect.height)
            self.ships.add(ship)

    def perp_level(self):
        """将等级转换为渲染的图像"""
        str_level = "Level: " + str(self.stats.level)
        self.level_image = self.font.render(str_level, True, self.text_color,
                                            self.ai_settings.bg_color)

        # 将得分放在屏幕左上角， 距边缘间隔20
        self.level_rect = self.level_image.get_rect()
        self.level_rect.left = self.screen_rect.left + 20
        self.level_rect.top = 20

    def perp_score(self):
        """将得分转换成一幅被渲染的图像"""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "Score: " + "{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color,
                                            self.ai_settings.bg_color)

        # 将得分放在屏幕右上角， 距边缘间隔20
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20

    def perp_high_score(self):
        """将得分转换成一幅被渲染的图像"""
        rounded_high_score = int(round(self.stats.high_score, -1))
        high_score_str = "Top: " + "{:,}".format(rounded_high_score)
        self.high_score_image = self.font.render(high_score_str, True,
                                                 self.text_color,
                                                 self.ai_settings.bg_color)

        # 将得分放在屏幕右上角， 距边缘间隔20
        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 20

    def show_score(self):
        """显示得分"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.high_score_image, self.high_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)
