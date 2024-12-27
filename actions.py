from database.database import database
from general.input_functions import NamedFunction, AskOption

def Quit():
    database.Close()
    exit(0)

def Export():
    StartExport(AskOption(export_table_options))

def RunQuery():
    database.query = input("Enter your query: \n")
    database.TryRunQuery()
    #if query succeeded: ask to export or not


#define main actions
main_actions = { 1 : NamedFunction("Quick Export", Export), 
                2 : NamedFunction("SQL Query", RunQuery), 
                3 : NamedFunction("Quit", Quit)}

#define export actions
export_table_options = {   
    1 : "Members",
    2 : "Scores",
    3 : "All"}

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
