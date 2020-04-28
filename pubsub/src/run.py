import sys, os
from core.process import *

class CoreFactory():
    newsCrawer = NewsCrawler()
    def run(self):
        self.newsCrawer.run(self)
    def stop(self):
        self.newsCrawer.stop(self)

if __name__ == '__main__':
    core = CoreFactory()
    core.run()
    print("End process")