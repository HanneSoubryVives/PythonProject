from database.database import database
from general.input_functions import NamedFunction, AskOption, ExecuteChoice

def Quit():
    database.Close()
    exit(0)

def Export():
    StartExport(AskOption(export_table_options))

def RunQuery():
    database.query = input("Enter your query: \n")
    succes = database.TryRunQuery()
    if succes: 
        ExecuteChoice(actions_after_query)

def Commit():
    database.Commit()

def Display():
    database.DisplaySelected()

def ExportQuery():
    output = AskOutputFile()
    try:
        database.ExportToExcel(output, database.query)
    except Exception as e:
        print(f"Exporting to excel has failed")
        print(e)

def DoNothing():
    pass

#define actions & options
main_actions = { 1 : NamedFunction("Quick Export", Export), 
                2 : NamedFunction("SQL Query", RunQuery), 
                3 : NamedFunction("Quit", Quit)}

export_table_options = {   
    1 : "Members",
    2 : "Scores",
    3 : "All"}

actions_after_query = {
    1 : NamedFunction("Commit change", Commit),
    2 : NamedFunction("Display selected", Display),
    3 : NamedFunction("Export selected", ExportQuery),
    4 : NamedFunction("Continue", DoNothing)
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
