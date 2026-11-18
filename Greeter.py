class Greeter:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return f"Hello, {self.name}! Welcome to OOP in Python."

if __name__ == "__main__":

    greeter = Greeter("Velasco")
    print(greeter.say_hello())