# Archery tool

### General description
This tool can help the archery club to keep the information about the club members 
and their results in the compititions. 
There is a database provided with some example data.

Member data: id, name, birthdate

Competition data: member id, date, discipline, distance, target size, score, nr arrows

### Functionality

#### Export to excel file:
Choose Export > Choose table > Choose file name/location. 
You can input just the file name (export to the project root folder) 
or a relative file path. The output will be a .xlsx-file.

### How to start
Create a virtual environment, activate it and install the packages from requirements.txt.

The database is already provided and the structure should stay the same.
If you want to move it to a different location, make sure to change the settings in general > settings.py. This database location is relative to the project root folder.
