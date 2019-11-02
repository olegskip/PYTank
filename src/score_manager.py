from label import Label
import config


class Score_Manager():
    def __init__(self, tanks_count):
        for i in range(tanks_count):
            self.texts_score.append(Label("0", config.score_font, config.score_fontSize, config.score_fontColor))

    def set_score(self, score):
        output = score.split(" ")
        if len(output) != len(self.texts_score):
            return False
        for i in range(len(output)):
            self.texts_score[i].set_text(output[i])
        return True

    texts_score = []
