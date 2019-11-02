from file import File
import config
from wall import Wall


class Level(File):
    def __init__(self, path):
        super().__init__(path)
        file_data = self.get_file_data()
        params = '\n'.join(file_data).split('\n')[0].split(",")
        self.walls_size = int(params[0])
        self.first_player_start_angle = int(params[1])
        self.second_player_start_angle = int(params[2])
        self.walls = []

        file_data.pop(0)

        global count_duplicate_vertical
        count_duplicate_vertical = 0

        global count_duplicate_horizontal
        count_duplicate_horizontal = 0

        for y in range(len(file_data)):
            for x in range(len(file_data[y])):

                # determinate positions
                if file_data[y][x] == str("1"):
                    self.first_player_start_pos = [x * self.walls_size, y * self.walls_size]
                elif file_data[y][x] == str("2"):
                    self.second_player_start_pos = [x * self.walls_size, y * self.walls_size]

                # drawing walls
                elif file_data[y][x] == str("-"):
                    try:
                        if file_data[y][x - 1] != "-":
                            count_duplicate_horizontal = 0
                    except IndexError:
                        pass

                    if count_duplicate_horizontal > 0:
                        count_duplicate_horizontal -= 1
                        continue

                    for temp_x in range(x, len(file_data[y])):
                        try:
                            if file_data[y][temp_x] == "-":
                                count_duplicate_horizontal += 1
                            else:
                                break
                        except IndexError:
                            break

                    if count_duplicate_horizontal > 0:
                        self.walls.append(Wall((self.walls_size * x - 3, self.walls_size * y),
                                               (self.walls_size * count_duplicate_horizontal + self.walls_size + self.walls_size * x + 3, self.walls_size * y),
                                               False, str(x) + str(y)))
                    else:
                        self.walls.append(Wall((self.walls_size * x - 3, self.walls_size * y),
                                               (self.walls_size + self.walls_size + self.walls_size * x + 3, self.walls_size * y),
                                               False, str(x) + str(y)))

                # draw a vertical wall
                elif file_data[y][x] == str("|"):
                    try:
                        if file_data[y - 1][x] != "|":
                            count_duplicate_vertical = 0
                    except IndexError:
                        pass

                    if count_duplicate_vertical > 0:
                        count_duplicate_vertical -= 1
                        continue

                    for temp_y in range(y, len(file_data)):
                        try:
                            if file_data[temp_y][x] == "|":
                                count_duplicate_vertical += 1
                            else:
                                break
                        except IndexError:
                            break

                    if count_duplicate_vertical > 0:
                        self.walls.append(Wall((self.walls_size + self.walls_size * x, self.walls_size * y),
                                               (self.walls_size + self.walls_size * x, self.walls_size * count_duplicate_vertical + self.walls_size * y),
                                               True, str(x) + str(y)))
                    else:
                        self.walls.append(Wall((self.walls_size + self.walls_size * x, self.walls_size * y),
                                               (self.walls_size + self.walls_size * x, self.walls_size + self.walls_size * y),
                                               True, str(x) + str(y)))

    first_player_start_pos = [0, 0]
    first_player_start_angle = 90

    second_player_start_pos = [0, 0]
    second_player_start_angle = 90
    walls_size = config.wall_size

    walls = []
