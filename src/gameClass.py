import pygame
from levelsManager import levelsManager
import config
import colors
from playerObject import playerObject
from wallObject import wallObject


class gameClass():
    window = pygame.display.set_mode(config.window_size, 0, 32)
    pygame.display.set_caption(config.window_name)
    gameDisplay = pygame.Surface(config.window_size)
    clock = pygame.time.Clock()
    walls = []
    balls = []
    players = []
    isOver = False

    lvlManager = levelsManager(config.PATH_TO_LEVELS)

    def __init__(self):
        pygame.init()
        print("\nLoading " + str(self.lvlManager.getCountOfLevels()) + " level(s) in " + self.lvlManager.getPathToFolder())
        for item in self.lvlManager.levels:
            try:
                item.getFileData()
            except FileNotFoundError:
                print("ERROR 404! " + item.getPath())
            else:
                print("Loading " + item.getPath())

        self.players.append(playerObject(config.first_player_rect, config.PATH_TO_IMAGES + '\\tank1.png'))
        self.players.append(playerObject(config.second_player_rect, config.PATH_TO_IMAGES + '\\tank2.png'))

        for i in range(len(levelsManager.levels[0].getFileData())):
            if levelsManager.levels[0].getFileData()[i] == str(1):
                self.walls.append(wallObject())


    def manageMoveKeyResult(self, key):
        if key[pygame.K_w]:
            self.players[0].movePlayerForward()
        if key[pygame.K_s]:
            self.players[0].movePlayerBack()
        if key[pygame.K_a]:
            self.players[0].movePlayerLeft()
        if key[pygame.K_d]:
            self.players[0].movePlayerRight()

        if key[pygame.K_UP]:
            self.players[1].movePlayerForward()
        if key[pygame.K_DOWN]:
            self.players[1].movePlayerBack()
        if key[pygame.K_LEFT]:
            self.players[1].movePlayerLeft()
        if key[pygame.K_RIGHT]:
            self.players[1].movePlayerRight()


    def manageBallResult(self, key):
        if key == pygame.K_t:
            self.players[0].addBall()
        if key == pygame.K_m:
            self.players[1].addBall()


    def update_scene(self):
        self.gameDisplay = pygame.display.set_mode(config.window_size)
        while not self.isOver:
            self.gameDisplay.fill(colors.background)

            self.checkForEvent()
            for player in self.players:
                if player.isAlive:
                    for ball in player.balls:
                        pygame.draw.circle(self.gameDisplay, colors.BLACK, (int(ball.rect.x), int(ball.rect.y)), ball.rect.height)
                        ball.updateBall()
                        if not ball.isEnable:
                            player.balls.remove(ball)
                        if pygame.sprite.collide_rect(player, ball):
                            player.isAlive = False

                    self.gameDisplay.blit(player.image, player.rect)

            pygame.display.update()

            self.clock.tick(60)

    def checkForEvent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.isOver = True
                return
            if event.type == pygame.KEYDOWN:
                self.manageBallResult(event.key)

        self.manageMoveKeyResult(pygame.key.get_pressed())
