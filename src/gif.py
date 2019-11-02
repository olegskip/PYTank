from file import get_folder_files_count
from timer import Timer
from image import Image


class Gif:
    def __init__(self, gif_path, rect, time):
        self.images = []
        frames_count = get_folder_files_count(gif_path)
        for i in range(frames_count):
            self.images.append(Image(gif_path + str(i) + ".png", rect))
        self.time = time

    def stop(self):
        self.is_stop = True

    def update(self, image):
        self.current_image = image

        if self.current_index >= len(self.images) - 1:
            self.current_index = 0
            self.current_image = Image()
        else:
            self.current_index += 1
        # check for auto repeat
        if not self.is_auto_repeat and self.current_index == 0 and not self.is_stop:
            self.current_image = Image()
            return None

        Timer(self.time, func=self.update, arg=[self.images[self.current_index]]).start_timer()

    def start_drawing(self):
        self.current_index = 0
        self.is_stop = False
        self.update(self.images[1])

    current_image = Image()
    images = []
    frames_count = 0
    current_index = 0
    time = 0
    is_auto_repeat = False
    is_stop = False
