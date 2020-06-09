from abc import ABCMeta, abstractmethod

class Message(metaclass=ABCMeta):
    @abstractmethod
    def process(self, worker):
        pass

class JobMessage(Message):
    def __init__(self, job, **kwargs):
        self.job = job
        self.data = kwargs

    def process(self, worker):
        worker.action(self.data)