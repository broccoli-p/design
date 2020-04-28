from abc import ABCMeta, abstractmethod

from urllib.request import urlopen
from bs4 import BeautifulSoup as bs
import re
import threading

from core.properties import WebProperty
from core.queue import WebQueue


class Worker(metaclass=ABCMeta):
    @abstractmethod
    def run(self):
        pass

    @abstractmethod
    def stop(self):
        pass

    @abstractmethod
    def process(self):
        pass

    @abstractmethod
    def polling(self):
        pass


class CrawlerWorker(Worker, WebProperty):
    def __init__(self):
        WebProperty.__init__()
        self.factory = factory
        self.config = WebProperty()
        self.queue = WebQueue()
        self.name = self.__class__.__name__
        print(self.config)

    def polling(self):
        pass

    def run(self):
        print("Run WebCrawler")
        t = threading.Thread(target=self.process, name=self.name, args=())
        self.thread = t
        t.daemon = True
        t.start()

    def process(self):
        while not self.quit:
            try:
                self.polling()
                found = self.queue.put(True, self.default_polling_interval)
                found.process(self)
            except queue.Empty:
                found = None
            except KeyboardInterrupt:
                found = None
                self.quit = True

    def stop(self):
        self.quit = True


class SenderWorker(Worker):
    def run(self):
        pass

    def stop(self):
        pass

    def process(self):
        pass

    def polling(self):
        pass

    