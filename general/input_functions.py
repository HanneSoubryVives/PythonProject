from sys import exit

#general functions
def CreateOptionStringFromStrings(options):
    give_options = "\nOptions: (input the number)\n"
    for index in range(1, len(options) + 1): 
    # +1 because end number is not included
        give_options += f"{index}. {options[index]}\n"

    return give_options

def CreateOptionStringFromNamedFunctions(options):
    give_options = "\nOptions: (input the number)\n"
    for index in range(1, len(options) + 1): 
    # +1 because end number is not included
        give_options += f"{index}. {options[index].name}\n"

    return give_options

def AskOptionLoop(option_string, options):
    valid_input = False
    while(not valid_input):
        # repeat question if invalid input
        try:
            chosen_option = int(input(option_string))
            if chosen_option not in options:
                raise Exception("This option number does not exist.")
            valid_input = True
        except ValueError:
            print("Please enter the number of an option.")
        except Exception as e:
            print(e)

    return chosen_option

def AskOption(options):
    return AskOptionLoop(CreateOptionStringFromStrings(options), options)

def ExecuteChoice(options):
    choice = AskOptionLoop(CreateOptionStringFromNamedFunctions(options), options)
    options[choice].function()

#Function wrapper
class NamedFunction():
    def __init__(self, name, function):
        self.name = name
        self.function = function