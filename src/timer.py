from threading import Thread
import time


class Timer:
    def __init__(self, selected_time, func=lambda: False, arg=None):
        if arg is None:
            arg = []
        self.selectedTime = selected_time
        self.selectedFunction = func
        self.isActive = False
        self.arg = arg

    def start_timer(self):
        self.isActive = True
        Thread(target=self.update_timer).start()

    def update_timer(self):
        start = time.time()
        while True:
            end = time.time()
            current_time = end - start

            if self.is_stop:
                self.isActive = False
                self.is_stop = False
                break

            if self.selectedTime <= current_time:
                if not self.arg:
                    self.selectedFunction()
                else:
                    self.selectedFunction(self.arg[0])
                self.isActive = False
                break
            time.sleep(1 / 10000000)

    main_thread = None
    selected_time = 0
    selected_function = lambda: None
    arg = []
    is_active = False
    is_stop = False
