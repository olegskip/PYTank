import pygame
import config
from player import Player
from timer import Timer
from levels_manager import *


class PlayersManager:
    def __init__(self):
        self.players.append(Player(config.first_player_rect, config.PATH_TO_IMAGES + '\\tank1.png', 0))
        self.players.append(Player(config.second_player_rect, config.PATH_TO_IMAGES + '\\tank2.png', 1))
        self.respawn_timer = Timer(config.player_time_spawn, func=self.spawn_players)

    players = []
    respawn_timer = None

    def reset(self):
        for player in self.players:
            player.reset()
        if self.respawn_timer.isActive:
            self.respawn_timer.stopTimer = True
        self.spawn_players()
        self.respawn_timer.is_stop = True

    def start_spawn_timer(self):
        if not self.respawn_timer.isActive:
            self.respawn_timer.start_timer()

    def spawn_players(self):
        lvlManager.update_index()
        self.update_victory_points()
        self.players[0].spawn()
        self.players[1].spawn()

        self.players[0].set_rect(config.first_player_rect)
        self.players[0].set_position(*lvlManager.levels[lvlManager.current_level_index].first_player_start_pos)
        self.players[0].set_angle(lvlManager.levels[lvlManager.current_level_index].first_player_start_angle)
        self.players[0].set_speed(config.first_player_speed, config.first_player_bullet_speed)
        self.players[0].set_save_distance(config.first_player_safe_distance)

        self.players[1].set_rect(config.second_player_rect)
        self.players[1].set_position(*lvlManager.levels[lvlManager.current_level_index].second_player_start_pos)
        self.players[1].set_angle(lvlManager.levels[lvlManager.current_level_index].second_player_start_angle)
        self.players[1].set_speed(config.second_player_speed, config.second_player_bullet_speed)
        self.players[1].set_save_distance(config.second_player_safe_distance)


    def update_victory_points(self):
        if self.players[0].is_alive and not self.players[1].is_alive:
            self.players[0].victory_points += 1

        elif self.players[1].is_alive and not self.players[0].is_alive:
            self.players[1].victory_points += 1

    def score_str(self):
        output = ""
        for player in self.players:
            output += str(player.victory_points) + " "
        return output.strip()

    def check_for_spawn(self):
        if not self.players[0].is_alive or not self.players[1].is_alive:
            self.start_spawn_timer()
            return True
        return False

    def check_for_kills(self):
        bullets = []
        for player in self.players:
            for bullet in player.bullets:
                bullets.append(bullet)

        for player in self.players:
            for bullet in bullets:
                if player.is_alive and bullet.check_for_touch(player.rect) and bullet.is_kill_player(player.id):
                    player.kill()
                    bullet.is_enable = False
                    self.check_for_spawn()

    def walls_collision(self, walls):
        for player in self.players:
            for bullet in player.bullets:
                for wall in walls:
                    if bullet.check_for_touch_wall(wall.rect, wall.id, wall.is_vertical):
                        break

    def manage_move_keys(self, key):
        if key[pygame.K_w]:
            self.players[0].move_forward()
        if key[pygame.K_s]:
            self.players[0].move_back()
        if key[pygame.K_a]:
            self.players[0].move_left()
        if key[pygame.K_d]:
            self.players[0].move_right()

        if key[pygame.K_UP]:
            self.players[1].move_forward()
        if key[pygame.K_DOWN]:
            self.players[1].move_back()
        if key[pygame.K_LEFT]:
            self.players[1].move_left()
        if key[pygame.K_RIGHT]:
            self.players[1].move_right()

    def manage_bullet_keys(self, key):
        if key == pygame.K_t:
            self.players[0].add_bullet()
        if key == pygame.K_m:
            self.players[1].add_bullet()

    # cheat codes
    def rainbow_cheat_code(self, is_active):
        if is_active:
            self.players[0].set_image(config.PATH_TO_IMAGES + '\\tank1_rainbow.png')
        else:
            self.players[0].set_image(config.PATH_TO_IMAGES + '\\tank1.png')
