class Hello:
    def __init__(self, str):
        self.str = str
class Goodbye(Hello):
    def __init__(self, str, name):
        super().__init__(str)
        self.name = name
    def say(self):
        print(f'{self.str}, {self.name}')

a = Goodbye('Hi', 'stranger')
a.say()