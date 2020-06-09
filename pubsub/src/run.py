from core import Crowler, Bot
import atexit

def foo():
    print('Ended process(call foo())')
    
atexit.register(foo)

class CoreFactory():
    def __init__(self):
        self.crowler = Crowler(self)
        self.bot = Bot()
    def run(self):
        self.crowler.run()
        self.bot.run()
    
    def stop(self):
        self.crowler.stop()
        self.bot.stop()

if __name__ == '__main__':
    try:
        global core
        core = CoreFactory()
        core.run()
    except KeyboardInterrupt:
        core.stop()
        print("Stop!!!")
    except Exception as err:
        print(err)