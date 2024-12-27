# Archery tool

### General description
This tool can help the archery club to keep the information about the club members 
and their results in the compititions. 
There is a database provided with sample data in the following tables:

members: member_id, first_name, last_name, birth_date

scores: member_id, date, discipline, distance, target_size, score, nr_arrows

### Functionality

#### Quick Export:
Choose Export > Choose table > Choose file name/location. 
You can input just the file name (export to the project root folder) 
or a relative file path. The output will be a .xlsx-file.

#### SQL Query:
Input your query. If the query was succesful you will get some options.
If it was a change > choose commit or continue (to discard change). Other options will not work.
If it was a select > choose display (in terminal), export (to excel) or continue (to do nothing).

Unfinished functions: 
- Only give the valid options depending on which query was given.
- Allow multiple options. (After a select query, first view in terminal and then export)


### How to start
Create a virtual environment, activate it and install the packages from requirements.txt.

The database is already provided and the structure should stay the same.
If you want to move it to a different location, make sure to change the settings in database > settings.py. This database location is relative to the project root folder.