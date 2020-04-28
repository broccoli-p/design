from abc import ABCMeta, abstractmethod
import yaml
import sys

class Property(metaclass=ABCMeta):
    @abstractmethod
    def get(self):
        pass

class PropertyA(property):
    def __init__(self, filename):
        with open(filename) as confd:
            self.config = yaml.safe_load(confd)

    def __getitem__(self, name):
        return self.config[name]

    def get(self):
        return self.config

    def __call__(self):
        return self.config
        
class DatabaseProperty(PropertyA):
    def __init__(self):
        super().__init__("config/database.yaml")

class WebProperty(PropertyA):
    def __init__(self):
        super().__init__("config/web.yaml")

class BotProperty(PropertyA):
    def __init__(self):
        super().__init__("config/bot.yaml")

class JobProperty(PropertyA):
    def __init__(self):
        super().__init__("config/job.yaml")
