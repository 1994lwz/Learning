#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
import pygame
from time import sleep

from bullet import Bullet
from alien import Alien


def check_high_score(stats, sb):
    """检查是否诞生了新的最高得分"""
    if stats.score > stats.high_score:
        stats.high_score = stats.score
        sb.prep_high_score()


def fire_bullet(screen, ship, bullets, ai_settings):
    """如果还没有达到子弹个数限制，就发射一颗子弹"""
    # 创建一颗子弹，兵将其加入到编组bullets中
    if len(bullets) < ai_settings.bullets_allowed:
        new_bullet = Bullet(screen, ship, ai_settings)
        bullets.add(new_bullet)


def check_keydown_events(event, screen, ship, bullets, ai_settings):
    """响应按键"""
    if (event.key == 27) or (event.key == pygame.K_q):
        sys.exit()
    elif event.key == pygame.K_RIGHT:
        ship.moving_right = True
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(screen, ship, bullets, ai_settings)


def check_keyup_events(event, ship):
    """响应松开"""
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(screen, sb, ship, aliens, bullets, stats, play_button, ai_settings):
    """响应按键和鼠标事件"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, screen, ship, bullets, ai_settings)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            check_play_button(screen, sb, ship, aliens, bullets, stats, play_button, mouse_x, mouse_y, ai_settings)


def check_play_button(screen, sb, ship, aliens, bullets, stats, play_button, mouse_x, mouse_y, ai_settings):
    """在玩家单击Play按钮时开始游戏"""
    # collidepoint检查鼠标单击位置是否在Play按钮的rect内
    button_clicked = play_button.rect.collidepoint(mouse_x, mouse_y)
    if button_clicked and not stats.game_active:
        # 重置游戏设置
        ai_settings.initialize_dynamic_settings()
        # 隐藏光标
        pygame.mouse.set_visible(False)
        # 重置游戏统计信息
        stats.reset_stats()
        stats.game_active = True

        # 重置记分牌图像
        sb.prep_score()
        sb.prep_high_score()
        sb.prep_level()
        sb.prep_ships()

        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，并让飞船居中
        creat_fleet(screen, aliens, ship, ai_settings)
        ship.center_ship()


def update_bullets(screen, stats, sb, ship, bullets, aliens, ai_settings):
    """更新子弹的位置，并删除已经消失的子弹"""
    bullets.update()
    for bullet in bullets.copy():  # 在for循环中，不应从列表或编组中删除条目
        if bullet.rect.bottom < 0:
            bullets.remove(bullet)

    check_bullet_alien_collisions(screen, stats, sb, ship, aliens, bullets, ai_settings)


def check_bullet_alien_collisions(screen, stats, sb, ship, aliens, bullets, ai_settings):
    """响应子弹和外星人的碰撞"""
    # 删除发生碰撞的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)
    # 该方法返回一个字典，key是发生碰撞的子弹，value是发生碰撞的外星人
    # 两个实参True告诉Pygame删除发生碰撞的子弹和外星人

    if collisions:
        for aliens in collisions.values():
            stats.score += ai_settings.alien_points * len(aliens)
            sb.prep_score()
        check_high_score(stats, sb)

    if len(aliens) == 0:
        # 删除现有的子弹并新建一群外星人
        bullets.empty()
        ai_settings.increase_speed()
        creat_fleet(screen, aliens, ship, ai_settings)

        # 如果整群外星人都被消灭，就提高一个等级
        stats.level += 1
        sb.prep_level()


def get_number_aliens_x(alien_width, ai_settings):
    """计算每行可容纳多少个外星人"""
    avaliable_space_x = ai_settings.screen_width - alien_width
    number_aliens_x = int(avaliable_space_x / (2 * alien_width) + 1)
    return number_aliens_x


def create_alien(screen, aliens, alien_number, row_number, ai_settings):
    """创建一个外星人并将其放在当前行"""
    alien = Alien(screen, ai_settings)
    alien_width = alien.rect.width
    alien.x = (alien_width / 2) + 2 * alien_width * alien_number + 9
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def creat_fleet(screen, aliens, ship, ai_settings):
    """创建外星人群"""
    # 创建一个外星人，并计算一行可容纳多少个外星人
    # 外星人间距为外星人宽度
    alien = Alien(screen, ai_settings)
    alien_width = alien.rect.width
    number_aliens_x = get_number_aliens_x(alien_width, ai_settings)
    number_rows = get_number_rows(ship.rect.height, alien.rect.height, ai_settings)

    # 创建外星人qun
    for row_number in range(number_rows - 1):
        for alien_number in range(number_aliens_x):
            create_alien(screen, aliens, alien_number, row_number, ai_settings)


def get_number_rows(ship_height, alien_height, ai_settings):
    """计算屏幕可容纳多少行外星人"""
    avaliable_space_y = (ai_settings.screen_height - alien_height
                         - ship_height)
    number_rows = int(avaliable_space_y / (2 * alien_height))
    return number_rows


def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘时采取相应的措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """将整群外星人下移，并改变它们的方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1


def ship_hit(screen, sb, ship, aliens, bullets, stats, ai_settings):
    """响应被外星人撞到的飞船"""
    # 将ships_left减1
    stats.ship_left -= 1

    # 更新记分牌
    sb.prep_ships()

    if stats.ship_left > 0:
        # 清空外星人列表和子弹列表
        aliens.empty()
        bullets.empty()

        # 创建一群新的外星人，并将飞船放到屏幕底端中央
        creat_fleet(screen, aliens, ship, ai_settings)
        ship.center_ship()

        # 暂停
        sleep(0.5)
    else:
        stats.game_active = False
        pygame.mouse.set_visible(True)


def check_aliens_bottom(screen, sb, ship, aliens, bullets, stats, ai_settings):
    """检查是否有外星人到达了屏幕底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom > screen_rect.bottom:
            # 像飞船被撞到一样进行处理
            ship_hit(screen, sb, ship, aliens, bullets, stats, ai_settings)
            break


def update_aliens(screen, sb, ship, aliens, bullets, stats, ai_settings):
    """
    检查是否有外星人位于屏幕边缘，并更新外星人群中所有外星人的位置
    """
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 检查外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):  # 该方法返回找到的第一个与飞船发生了碰撞的外星人
        ship_hit(screen, sb, ship, aliens, bullets, stats, ai_settings)
        # print("Ship Hit!!!")
    # 检查是否有外星人到达屏幕底端
    check_aliens_bottom(screen, sb, ship, aliens, bullets, stats, ai_settings)


def update_screen(screen, stats, sb, ship, bullets, aliens, play_button, ai_settings):
    """更新屏幕上的图像，并切换到新屏幕"""
    # 每次循环时都重绘屏幕
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    aliens.draw(screen)  # 对编组调用draw()时，Pygame自动绘制编组的每个元素，绘制位置由元素的属性rect决定

    # 显示得分
    sb.show_score()

    # 在飞船和外星人后面绘制所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()

    # 如果游戏处于非活动状态，就绘制Play按钮
    if not stats.game_active:
        play_button.draw_button()

    # 刷新新屏幕，使屏幕事件平滑过渡
    pygame.display.flip()
