from general.actions import * #import everything from this file
from general.settings import *
from database.database import Database as db

#initialize database
database = db(databaseFile)

#start program
while(True):

	# ask action
	give_options = "\nSelect action:\n"
	for action in list(Action):
		give_options += f"{action.value}. {action.name}\n"

	valid_input = False
	while(not valid_input):
		# repeat question if invalid input
		try:
			chosen_action = int(input(give_options))
			if chosen_action not in Action:
				raise Exception("This action number does not exist.")
			valid_input = True
		except ValueError:
			print("Please enter the number of an action.")
		except Exception as e:
			print(e)

	# execute matching functionality
	if chosen_action in action_functions:
		action_functions[chosen_action]()
	else:
		print("Warning: action functionality not found.")
