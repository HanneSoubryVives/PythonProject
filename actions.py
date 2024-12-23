from database.database import Database as db
from general.settings import * #import everything from this file
from general.input_functions import *

#initialize database
database = db(databaseFile)

#must stay at the top of the file (because used to define actions)
def Quit():
    database.Close()
    exit(0)

def Export():
    StartExport(AskOption(export_table_options))

def testFunction2():
    print("Testfunction executed!")

#define main actions
main_actions = { 1 : NamedFunction("Export", Export), 
                2 : NamedFunction("Modify", testFunction2), 
                3 : NamedFunction("Quit", Quit)}

#define export actions
export_table_options = {   
    1 : "Members",
    2 : "Scores",
    3 : "All"}

#define modify actions
modify_actions = {
    1 : "Change",
    2 : "Add",
    3 : "Delete"}

#other functions
#needs database access
def StartExport(exportOptionsNumber):
    output = input("Excel output file?\n")
    if not output.endswith(".xlsx"):
        output += ".xlsx"

    try:
        table = export_table_options[exportOptionsNumber]
        database.ExportToExcel(output, database.exportOptions[table])
    except Exception as e:
        print(f"Exporting to excel has failed")
        print(e)
