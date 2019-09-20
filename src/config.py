from fileObject import getExePath
import pygame
from imageObject import imageObject

PATH_TO_LEVELS = getExePath() + "\\levels"
PATH_TO_IMAGES = getExePath() + "\\images"
PATH_TO_BALL = PATH_TO_IMAGES + "\\ball.png"

window_name = "Tanks..."

window_size = (700, 700)

first_player_rect = pygame.Rect(200, 100, 45, 75)
first_player_speed = 7
first_player_bullet_speed = 10
first_player_safe_distance = 75  # if sprite was not changed - do not change this value!

second_player_rect = pygame.Rect(300, 300, 35, 70)
second_player_speed = 9
second_player_bullet_speed = 6
second_player_safe_distance = 90  # if sprite was not changed - do not change this value!


ball_radius = 5
ball_image = imageObject(PATH_TO_BALL, size=(ball_radius, ball_radius)).image
