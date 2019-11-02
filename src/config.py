from file import get_exe_path
import pygame
from image import Image
import colors

# the window properties
window_name = "Tanks..."
window_size = (1000, 700)

# set up paths for files
PATH_TO_LEVELS = get_exe_path() + "\\levels"
PATH_TO_IMAGES = get_exe_path() + "\\images"
ICON_PATH = PATH_TO_IMAGES + "\\icon.png"
PATH_TO_EFFECTS = get_exe_path() + "\\effects"
PATH_TO_BALL = PATH_TO_IMAGES + "\\ball.png"
PATH_TO_FONTS = get_exe_path() + "\\fonts"

# the score
score_font = PATH_TO_FONTS + "\\DroidSerif.ttf"
score_fontColor = colors.BLACK
score_fontSize = 35

# cheat codes properties
cheatCode_activateText = "Cheat code activated!"
cheatCode_deactivateText = "Cheat code dectivated!"
cheatCode_font = PATH_TO_FONTS + "\\PriceDown.ttf"
cheatCode_fontColor = colors.BLACK
cheatCode_backgroundColor = None
cheatCode_fontSize = 40

# players parameters
first_player_rect = pygame.Rect(400, 300, 30, 50)
first_player_speed = 5
first_player_bullet_speed = 5
first_player_safe_distance = 10

second_player_rect = pygame.Rect(200, 400, 30, 50)
second_player_speed = 5
second_player_bullet_speed = 5
second_player_safe_distance = 10

player_time_spawn = 2  # in secs

# a wall parameters
wall_width = 7
wall_size = 50
wall_margin = 75

# a ball parameters
ball_radius = 5
ball_image = Image(PATH_TO_BALL, size=(ball_radius, ball_radius)).image
ball_spawn_time = 10
max_ball_count = 5
