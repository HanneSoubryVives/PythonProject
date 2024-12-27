from database.database import database
from general.input_functions import NamedFunction, AskOption

def Quit():
    database.Close()
    exit(0)

def Export():
    StartExport(AskOption(export_table_options))

def RunQuery():
    database.query = input("Enter your query: \n")
    succes = database.TryRunQuery()
    if succes: 
        choice = AskOption(export_question)
        if choice == 1:
            output = AskOutputFile()
            try:
                database.ExportToExcel(output, database.query)
            except Exception as e:
                print(f"Exporting to excel has failed")
                print(e)


#define actions & options
main_actions = { 1 : NamedFunction("Quick Export", Export), 
                2 : NamedFunction("SQL Query", RunQuery), 
                3 : NamedFunction("Quit", Quit)}

export_table_options = {   
    1 : "Members",
    2 : "Scores",
    3 : "All"}

export_question = {
    1 : "Export result",
    2 : "Continue without export"
}

#other functions
#needs database access
def AskOutputFile():
    output = input("Excel output file?\n")
    if not output.endswith(".xlsx"):
        output += ".xlsx"

    return output

def StartExport(exportOptionsNumber):
    output = AskOutputFile()
    try:
        table = export_table_options[exportOptionsNumber]
        database.ExportToExcel(output, database.exportOptions[table])
    except Exception as e:
        print(f"Exporting to excel has failed")
        print(e)
