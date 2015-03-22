#!/usr/bin/python
# -*- coding: utf-8 -*-

#****************************************************
# nach  Reimar Barnstorf www.7soft.de                   *
#****************************************************

# Python Imports
import os
import pygame
import sys
import time

#used Variables:
#brightness
#Tmin
#Tmax
#Tfeel
#WakeTime
#WeatherIcon

#Display normal Watch interface
def DisplayWatch(brightness, Tmin, Tmax, Tfeel, WakeTime, WeatherIcon):
    pygame.init()
    window = pygame.display.set_mode((320,240))
    font0 = pygame.font.SysFont("droidsans", 21)
    font1 = pygame.font.SysFont("droidsans", 83)
    font2 = pygame.font.SysFont("freemono", 33)
    font3 = pygame.font.SysFont("freemono", 26)
    font2.set_italic(1)
    font2.set_bold(1)
    label0 = font0.render("WECKER-Test", 1, (255,0,0))
    label3 = font3.render("13°C ", 1, (255,0,0))
    #rect1 = pygame.Rect(0, 100, 319, 30)
    #roter Balken
    #rect2 = pygame.Rect(0, 150, 319, 35)
    #tuerkieser Balken hinter Datum
    WetterIcon = pygame.image.load(os.path.join('/home/pi/WetterIcons/vcloudsDevianart', WeatherIcon + '.png'))
    os.system("tft_init")
    os.system("tft_clear")
    os.system("tft_pwm 80")
    window.fill(pygame.Color(0,0,0))
    #pygame.draw.rect(window, pygame.Color(60,0,0), rect1)
    #pygame.draw.rect(window, pygame.Color(0,200,200), rect2)
    pygame.draw.line(window, pygame.Color(0,0,255), (0,210), (319,210))
    pygame.draw.line(window, pygame.Color(0,0,255), (0,239), (319,239))
    lt = time.localtime()
    label1 = font1.render(time.strftime("  %H:%M ", lt), 1, (255,255,0))
    label2 = font2.render(time.strftime("%a %d.%m.%Y ", lt), 1, (255,255,0))
    window.blit(label2, (0,90))
    window.blit(label1, (0,0))
    window.blit(label3, (10,210))
    window.blit(label0, (0,127))
    window.blit(WetterIcon, (146,119))
    pygame.image.save(window, "/ram/temp.bmp")
    os.system("tft_bmp /ram/temp.bmp")
