class CheatCodeHandler:
    def manage_keys(self, key):
        self.last_keys.append(key)

        for cheatCode in self.cheatCodes:
            if len(cheatCode.keys) <= len(self.last_keys):
                is_keys_true = True
                for i in range(1, len(cheatCode.keys) + 1):
                    if self.last_keys[-(len(cheatCode.keys) - i + 1)] != ord(cheatCode.keys[i - 1]):
                        is_keys_true = False

                if is_keys_true:
                    cheatCode.activate()

    cheatCodes = []
    last_keys = []
