from fileObject import getExePath
import pygame

PATH_TO_LEVELS = getExePath() + "\levels"
PATH_TO_IMAGES = getExePath() + "\images"

window_name = "Tanks..."

window_size = (700, 700)

first_player_rect = pygame.Rect(300, 100, 40, 70)
second_player_rect = pygame.Rect(50, 50, 40, 70)


ball_radius = 5