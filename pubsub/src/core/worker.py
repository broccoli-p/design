
#-*-coding:utf-8-*-
from abc import ABCMeta, abstractmethod
import multiprocessing as mp
#mp.set_start_method('spawn')

import threading
import queue


ST = 5

class Worker(metaclass=ABCMeta):
    def __init__(self):
        self.running = False
    '''
    @abstractmethod
    def run(self):
        pass
    '''
    def run(self):
        self.running = True
        self.p = mp.Process(target=self.process, name=self.name, args=())
        #self.thread = threading.Thread(target=self.process, name=self.name)
        #self.thread.daemon = True
        self.p.start()
    
    @abstractmethod
    def process(self):
        pass

    @abstractmethod
    def polling(self):
        pass

    @abstractmethod
    def wait(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class SubWorker(Worker, metaclass=ABCMeta):  
    @abstractmethod  
    def action(self, kwargs):
        pass

class Publisher(Worker):
    def __init__(self):
        super().__init__()
        self.name = self.__class__.__name__
        self.sleep_event = threading.Event()
    '''      
    def run(self):
        self.running = True
        self.process = mp.Process(target=self.process, name=self.name, args=())
        #self.thread = threading.Thread(target=self.process, name=self.name)
        #self.thread.daemon = True
        self.process.start()
    '''

    def process(self):
        '''
        실제 동작을 하는 프로세스 
        self.running 가 false 될떄까지 동작한다.
        self.polling()를 실행시키는 역할
        '''
        while self.running:
            try:
                self.wait(ST)
                self.polling()
            except KeyboardInterrupt:
                self.running = False
            except Exception as err:
                print("Pub error:", err)
    
    def wait(self, t):
        self.sleep_event.wait(t)

    def stop(self):
        self.running = False
        

class Subscriber(SubWorker):
    def __init__(self):
        super().__init__()
        self.msg_queue = mp.Queue()
        self.name = self.__class__.__name__
    '''
    def run(self):
        self.thread = threading.Thread(target=self.process, name=self.name)
        self.thread.daemon = True
        self.thread.start()
    '''            
    def stop(self):
        pass

    def polling(self):
        pass

    def wait(self):
        pass

    def process(self):
        while self.running:
            try:
                if self.msg_queue.qsize() >= 2:
                    for i in range(self.msg_queue.qsize()):
                        msg = self.msg_queue.get(True, i)
                        msg.process(self)
            except KeyboardInterrupt:
                self.running = False
            except queue.Empty:
                pass
            except Exception as err:
                print("Sub error:",err)
