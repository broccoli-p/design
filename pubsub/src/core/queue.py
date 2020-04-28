import queue
from core.message import JobMessage
from core.properties import JobProperty

jobConfig = JobProperty()

class Queue():
    def __init__(self):
        self.queue = queue.Queue()

    def get(self):
        return self.queue.get(True, jobConfig['server']['timeout'])

class JobQueue(Queue):
    def put(self, job, obj):
        self.queue.put(JobMessage(job, obj))

class WebQueue():
    def put(self, job, obj):
        self.queue.put(WebMessage(job, obj))