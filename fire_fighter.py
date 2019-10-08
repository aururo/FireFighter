#encoding:utf-8

#创建pygame窗口以及响应用户输入
import pygame
from pygame.sprite import Group
#导入类Settings
from settings import Settings

#导入类Ship
from base_ship.t50_ship import *

#导入模块game_functions
import game_functions as gf

#导入类Alien

from game_stats import GameStats
from scoreboard import Scoreboard
from button import Button
from base_ship.t50_ship import *
from base_ship.j20_ship import *

def run_game():
    #初始化游戏并创建一个屏幕对象
    pygame.init()   #初始化背景设置
    ai_settings = Settings()
    """
    设置窗口大小, 返回surface对象，表示整个游戏窗口
    """
    game_screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    #创建游戏标题
    pygame.display.set_caption("Fire Fighter")

    #创建游戏按钮
    play_button = Button(ai_settings, game_screen, "Start")

    #创建一个用于存储游戏统计信息的实例， 并创建记分牌
    game_stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, game_screen, game_stats)

    #创建一艘飞船
    t50_ship = T50_Ship(ai_settings, game_screen)
    j20_ship = J20_Ship(ai_settings, game_screen)

    #创建一个用于存储子弹的编组
    bullets = Group()

    aliens = Group()
    #创建外星人群
    gf.create_fleet(ai_settings, game_screen, t50_ship, aliens)

    #背景音乐
    pygame.mixer.music.load("sounds/111.mp3")
    pygame.mixer.music.play(loops=-1, start=0.0)
    music1 = pygame.mixer.Sound("sounds/222.wav")

    #开始游戏的主循环
    while True:
        #监视键盘和鼠标事件
        gf.check_events(ai_settings, game_screen, game_stats, play_button, t50_ship, aliens, bullets, music1, sb)

        if game_stats.game_active:     #判断是否处于活动状态（是否有命）

            #根据移动标志调整飞船的位置
            t50_ship.update()
            j20_ship.update()

            # 更新子弹位置并删除已消失的子弹  删除子弹击中的外星人
            gf.update_bullets(ai_settings, game_screen, game_stats, sb, t50_ship, aliens, bullets)

            #更新外星人位置
            gf.update_aliens(ai_settings, game_stats, game_screen, t50_ship, aliens, bullets)

        # 更新屏幕上的图像，并切换到新屏幕
        gf.update_screen(ai_settings, game_screen, game_stats, sb, t50_ship, aliens, bullets, play_button)

run_game()

