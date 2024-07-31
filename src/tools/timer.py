import time, datetime
from mixpanel import Mixpanel

MIXPANEL_TOKEN = "346d4167f1fe0646eac6d15876ecf2c8"
USER_ID = "shaulc@questarauto.com"
EVENT_NAME = "performance"

class Timer():
    def __init__(self, config) -> None:
        self.my_mixpanel = Mixpanel(MIXPANEL_TOKEN)
        self._private_build_config_details(config)

    def _private_build_config_details(self, config):
        new_config = {
            "env_name":config["env_name"],
            "url":config["URL"],
            "user_name":config["user"]["name"]
        }
        self.attributes = new_config

    def start(self):
        self.start_time = time.time()
        self.date = datetime.date.today()

    def end(self, message:str):
        self.time_elapsed = (time.time() - self.start_time)
        self.attributes['duration_time_ms'] = int(self.time_elapsed * 1000) # time in ms
        print(message +f"  ({self.time_elapsed:.3f} sec)" + f" {self.date}")

    def logEvent(self,event_name:str):
        print("logging event")
        properties = self.attributes.copy()
        properties['page'] = event_name
        self.my_mixpanel.track(USER_ID, EVENT_NAME, properties)