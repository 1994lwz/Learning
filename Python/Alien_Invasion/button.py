#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pygame.font  # pygame渲染文本到屏幕上


class Button():

    def __init__(self, msg, screen, ai_settings):
        """初始化按钮的属性"""
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 设置按钮的尺寸和其他属性
        self.width, self.height = 130, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        # 制定使用什么文字来渲染文本，实参None让pygame使用默认字体，48指定了文本的字号
        self.font = pygame.font.SysFont(None, 48)

        # 创建按钮的rect对象，并使其居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 按钮的标签只需要创建一次
        self.prep_msg(msg)

    def prep_msg(self, msg):
        """将msg选人为图像，并使其在按钮上居中"""

        # 方法font.render()将存储在msg中的文本转换为图像
        # 该方法接受一个布尔实参，该实参制定开启还是关闭反锯齿功能（反锯齿让文本的边缘更平滑）
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # 绘制一个用颜色填充的按钮，再绘制文本
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
