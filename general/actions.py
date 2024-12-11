from sys import exit
from enum import Enum

class Action(Enum):
    Quit = 1
    Test1 = 2
    Test2 = 3

def quit():
    exit(0)

def testFunction():
    print("Testfunction executed!")

action_functions = {
    Action.Quit.value: quit,
    Action.Test1.value: testFunction
}