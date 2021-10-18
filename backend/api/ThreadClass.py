
import threading
 
class TaskThread(threading.Thread):
    def __init__(self, func, args=()):
        super(TaskThread, self).__init__()
        self.func = func
        self.args = args
 
    def run(self):
        self.result = self.func(*self.args)
 
    def get_result(self):
        threading.Thread.join(self) # 等待线程执行完毕
        try:
            return self.result
        except Exception as e:
            print('[ERROR] in TaskThread ', e)
            return None