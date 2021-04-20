#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# import sys
import pygame
from pygame.sprite import Group

from ship import Ship
from button import Button
import game_functions as gf
from settings import Settings
from game_stats import GameStats
from scoreboard import Scoreboard


# from alien import Alien

def run_game():
    """主程序"""
    # 初始化游戏并创建一个屏幕对象
    pygame.init()  # 初始化背景设置
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))  # 创建 1100 * 700 的游戏窗口
    pygame.display.set_caption("Alien_Invasion")

    # 创建Play按钮
    play_button = Button("Play", screen, ai_settings)

    # 创建一艘飞船
    ship = Ship(screen, ai_settings)
    # 创建一个用于存储游戏统计信息的实例, 并创建记分牌
    stats = GameStats(ai_settings)
    sb = Scoreboard(stats, screen, ai_settings)
    # 创建一个外星人编组并创建外星人群
    aliens = Group()
    gf.creat_fleet(screen, aliens, ship, ai_settings)
    # 创建一个用于存储子弹的编组
    bullets = Group()

    # 设置背景色
    # bg_color = (230 ,230 ,230)

    # 开始游戏的主循环
    while True:
        # 监视键盘和鼠标事件，并绘制飞船刷新屏幕
        gf.check_events(screen, sb, ship, aliens, bullets, stats, play_button, ai_settings)
        if stats.game_active:
            ship.update()
            gf.update_bullets(screen, stats, sb, ship, bullets, aliens, ai_settings)
            gf.update_aliens(screen, sb, ship, aliens, bullets, stats, ai_settings)

        gf.update_screen(screen, stats, sb, ship, bullets, aliens, play_button, ai_settings)


run_game()
