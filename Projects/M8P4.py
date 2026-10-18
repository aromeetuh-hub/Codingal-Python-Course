class Robot:
    def __init__(self, name, model):
        self.name = name
        self.model = model

    def introduce(self):
        print(f"Hello! My name is {self.name}.")
        print(f"I am a {self.model} robot.")


my_robot = Robot("Robo", "helper")
my_robot.introduce()