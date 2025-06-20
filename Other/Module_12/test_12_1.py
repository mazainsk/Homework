# Original code from GitHub:
# https://github.com/yanchuki/HumanMoveTest/blob/master/runner.py


class Runner:
    def __init__(self, name):
        self.name = name
        self.distance = 0

    def run(self):
        self.distance += 10

    def walk(self):
        self.distance += 5

    def __str__(self):
        return self.name