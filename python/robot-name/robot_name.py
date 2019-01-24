import random
from string import ascii_uppercase

class Robot():
    __used_names__ = set()

    def __init__(self):
        self.reset()

    def reset(self):
        self.name = self.get_fresh_name()

    def get_fresh_name(self):
        name = self.generate_name()

        while self.__used_names__.__contains__(name):
            name = self.generate_name()
        self.__used_names__.add(name)

        return name

    @staticmethod
    def generate_name():
        "This function generates a random name"
        random_chars = random.choice(ascii_uppercase) + random.choice(ascii_uppercase)
        random_digits = "{}".format(int(random.random() * 100)).zfill(3)
        return "{}{}".format(random_chars, random_digits)
