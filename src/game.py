import pygame
from levels_manager import *
import config
import colors
from players_manager import PlayersManager
from score_manager import Score_Manager
from cheat_code import CheatCode
from cheat_code_handler import CheatCodeHandler


class Game:
    window = pygame.display.set_mode(config.window_size, 0, 32)
    pygame.display.set_caption(config.window_name)
    gameDisplay = pygame.Surface(config.window_size)
    clock = pygame.time.Clock()

    is_over = False
    is_pause = False
    players_manager = PlayersManager()
    score = 0
    gif = None

    cheats_manager = CheatCodeHandler()

    def __init__(self):
        pygame.init()
        self.score = Score_Manager(2)
        self.players_manager.spawn_players()
        self.players_manager.players[0].set_angle(lvlManager.levels[lvlManager.current_level_index].first_player_start_angle)
        self.players_manager.players[1].set_angle(lvlManager.levels[lvlManager.current_level_index].second_player_start_angle)
        self.players_manager.players[0].set_position(*lvlManager.levels[lvlManager.current_level_index].first_player_start_pos)
        self.players_manager.players[1].set_position(*lvlManager.levels[lvlManager.current_level_index].second_player_start_pos)

        self.players_manager.spawn_players()

        self.cheats_manager.cheatCodes.append(CheatCode(['c', 'x', 'c'], self.players_manager.rainbow_cheat_code))

        # set up the icon
        pygame.display.set_icon(pygame.image.load(config.ICON_PATH).convert_alpha())

    def restart(self):
        self.players_manager.reset()

    def update_scene(self):
        self.gameDisplay = pygame.display.set_mode(config.window_size)

        # init walls
        for wall in lvlManager.levels[lvlManager.current_level_index].walls:
            wall.set_up_init_params(pygame.draw.line(self.gameDisplay, colors.GREEN, wall.start_pos, wall.end_pos, config.wall_width),
                                    self.gameDisplay.subsurface(pygame.draw.line(self.gameDisplay, colors.GREEN, wall.start_pos, wall.end_pos, config.wall_width)))
        while not self.is_over:
            self.gameDisplay.fill(colors.background)

            self.event_handler()
            if not self.is_pause:
                # draw players
                for player in self.players_manager.players:
                    for bullet in player.bullets:
                        pygame.draw.circle(self.gameDisplay, colors.BLACK, (int(bullet.rect.x), int(bullet.rect.y)), bullet.rect.height)
                        bullet.update_bullet()
                        if not bullet.is_enable:
                            player.bullets.remove(bullet)
                    if player.is_alive:
                        self.gameDisplay.blit(player.image, player.rect)

                    # draw the death gif
                    if not player.death_gif.is_stop:
                        self.gameDisplay.blit(player.death_gif.current_image.image, player.rect)

                for wall in lvlManager.levels[lvlManager.current_level_index].walls:
                    pygame.draw.line(self.gameDisplay, colors.GREEN, wall.start_pos, wall.end_pos, config.wall_width)

                self.players_manager.walls_collision(lvlManager.levels[lvlManager.current_level_index].walls)

                # manage the score
                self.score.set_score(self.players_manager.score_str())
                for i in range(len(self.score.texts_score)):
                    self.gameDisplay.blit(self.score.texts_score[i].text_obj, (5+50*i, 0))

                # manage the cheat codes
                for item in self.cheats_manager.cheatCodes:
                    if item.message.is_show:
                        self.gameDisplay.blit(item.message.text_obj, (config.window_size[0] / 2 - item.message.text_obj.get_rect().width / 2, config.window_size[1] / 2 - item.message.text_obj.get_rect().height / 2 - 100))

                self.players_manager.check_for_kills()

                pygame.display.flip()
                self.clock.tick(60)

    def event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.is_over = True
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_F6:
                    self.is_pause = not self.is_pause
                elif not self.is_pause:
                    self.players_manager.manage_bullet_keys(event.key)
                    self.cheats_manager.manage_keys(event.key)
                if event.key == pygame.K_F5:
                    self.restart()

        if not self.is_pause:
            self.players_manager.manage_move_keys(pygame.key.get_pressed())
