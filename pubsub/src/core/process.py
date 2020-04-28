from core.worker import *

class NewsCrawler(CrawlerWorker):
    def __init__(self, core):
        self.core = core
        super().__init__()

    def polling(self):
        
            