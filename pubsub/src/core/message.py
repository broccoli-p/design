from abc import ABCMeta, abstractmethod

class Message(metaclass=ABCMeta):
    @abstractmethod
    def process(self, worker):
        pass

class JobMessage(Message):
    def __init__(self, job, obj):
        self.job = job
        self.information = obj

    def process(self, worker):
        print("JobMessage")

class WebMessage(Message):
    def __init__(self, job, obj):
        self.job = job
        self.information = obj

    def process(self, worker):
        worker.crawler()

class QuitMessage(Message):
    def process(self,worker):
        worker.quit()