from sys import exit
from enum import Enum
from database.database import Database as db
from general.settings import * #import everything from this file

#initialize database
database = db(databaseFile)

#Loop
def ActionLoop(actionOptions, actionFunctions):
    # ask action
    give_options = "\nSelect action:\n"
    for action in list(actionOptions):
        give_options += f"{action.value}. {action.name}\n"

    valid_input = False
    while(not valid_input):
        # repeat question if invalid input
        try:
            chosen_action = int(input(give_options))
            if chosen_action not in actionOptions:
                raise Exception("This action number does not exist.")
            valid_input = True
        except ValueError:
            print("Please enter the number of an action.")
        except Exception as e:
            print(e)

    # execute matching functionality
    if chosen_action in actionFunctions:
        actionFunctions[chosen_action]()
    else:
        print("Warning: action functionality not found.")

#Main actions
class MainAction(Enum):
    Export = 1
    Test2 = 2
    Quit = 3

def quit():
    exit(0)

def ExportMembers():
    ActionLoop(ExportAction, export_action_functions)

def testFunction2():
    print("Testfunction executed!")

main_action_functions = {
    MainAction.Quit.value: quit,
    MainAction.Export.value: ExportMembers,
    MainAction.Test2.value: testFunction2,
}

#Export actions
class ExportAction(Enum):
    Members = 1
    Scores = 2
    All = 3

def StartExportMembers():
    output = input("Output file: ")
    database.ExportMembers(output)

export_action_functions = {
    ExportAction.Members.value: StartExportMembers
}