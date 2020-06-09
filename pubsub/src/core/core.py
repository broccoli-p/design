from worker import Publisher, Subscriber
from message import JobMessage
import os, time

class Crowler(Publisher):
    def __init__(self, core):
        self.core = core
        super().__init__()

    def polling(self):
        filename = 'tmp.txt'
        pid = os.getpid()
        now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
        with open(filename, 'w') as fd:
            fd.write(f'Hello {now}:{pid}!!!\n')
        self.core.bot.msg_queue.put(JobMessage('ReadFile', PATH=filename))


class Bot(Subscriber):
    def __init__(self):
        super().__init__()
    
    def action(self, kwargs):
        print("Start Action!!!")
        assert('PATH' in kwargs)
        with open(kwargs['PATH'], 'r') as fd:
            content = fd.read()
            print(content)
        
