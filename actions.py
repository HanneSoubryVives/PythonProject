from sys import exit
from enum import Enum
from database.database import Database as db
from general.settings import * #import everything from this file

#initialize database
database = db(databaseFile)

#Loop
def ActionLoop(actionOptions, actionFunctions):
    # ask action
    give_options = "\nSelect action (input the number):\n"
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
    Modify = 2
    Quit = 3

def quit():
    exit(0)

def ExportLoop():
    ActionLoop(ExportAction, export_action_functions)

def testFunction2():
    print("Testfunction executed!")

main_action_functions = {
    MainAction.Quit.value: quit,
    MainAction.Export.value: ExportLoop,
    MainAction.Modify.value: testFunction2,
}

#Export actions
class ExportAction(Enum):
    Members = 1
    Scores = 2
    All = 3

def StartExport(exportOptionsKey):
    output = input("Excel output file?\n")
    if not output.endswith(".xlsx"):
        output += ".xlsx"

    try:
        database.Export(output, database.exportOptions[exportOptionsKey])
    except Exception as e:
        print(f"Exporting to excel has failed")
        print(e)

def ExportMembers():
    StartExport("Members")

def ExportScores():
    StartExport("Scores")

def ExportAll():
    StartExport("All")
    
export_action_functions = {
    ExportAction.Members.value: ExportMembers,
    ExportAction.Scores.value: ExportScores,
    ExportAction.All.value: ExportAll
}