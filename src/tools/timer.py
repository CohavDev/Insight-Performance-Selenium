import time
class Timer():
    def __init__(self) -> None:
        pass

    def start(self):
        self.start_time = time.time()
    def end(self, message:str):
        time_elapsed = (time.time() - self.start_time)
        print(message +f"  ({time_elapsed:.3f} sec)")