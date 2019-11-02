from label import Label
import config
from timer import Timer


class CheatCode:
    def __init__(self, keys, function):
        self.keys = keys
        self.execute_function = function

        self.message = Label(config.cheatCode_activateText, config.cheatCode_font, config.cheatCode_fontSize, config.cheatCode_fontColor, config.cheatCode_backgroundColor)
        self.message_timer = Timer(3, func=self.deactivate)

    def activate(self):
        self.is_active = not self.is_active
        if self.is_active:
            self.message = Label(config.cheatCode_activateText, config.cheatCode_font, config.cheatCode_fontSize,config.cheatCode_fontColor, config.cheatCode_backgroundColor)
        else:
            self.message = Label(config.cheatCode_deactivateText, config.cheatCode_font, config.cheatCode_fontSize,config.cheatCode_fontColor, config.cheatCode_backgroundColor)
        self.execute_function(self.is_active)
        self.message.is_show = True
        if not self.message_timer.is_active:
            self.message_timer.start_timer()

    def deactivate(self):
        self.message.isShow = False

    message_timer = None

    message = None
    activate_message = None
    deactivate_message = None

    is_active = False
    keys = []
    execute_function = lambda: False