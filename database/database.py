from database.settings import databaseFile
import sys
import sqlite3
from pathlib import Path
import pandas as pd 

class Database():
	def __init__(self, databaseFile):
		self.exportOptions = {
		"Members": "SELECT * FROM members",
		"Scores": "SELECT * FROM scores",
		"All": "SELECT * FROM members JOIN scores using(member_id)"}
		self.query = ""

		self.ConnectDatabase(databaseFile)

	def ConnectDatabase(self, databaseFile):
		#move to root folder, then add the file location
		self.__parent_dir = Path(__file__).parent.parent.absolute()
		databaseFile = self.__parent_dir / databaseFile

		#make connection
		try:
			self.__db = sqlite3.connect(databaseFile)
			self.__cursor = self.__db.cursor()
		except Exception as e:
			print(f"Connecting to database has failed:\n{e}")
			sys.exit(1)

	#cleanup
	def Close(self):
		self.__cursor.close()
		self.__db.close()

	#pandas
	def QueryResultToPandas(self, result):
		#get and clean column names
		columns = [description[0] for description in self.__cursor.description]

		#row data output from cursor -> column data input for pandas
		data = {}
		for index in range(0, len(columns)): 
			columns[index] = columns[index].replace("_", " ").capitalize()
			data[columns[index]] = [row[index] for row in result]

		self.__dataframe = pd.DataFrame(data)

	#functionality
	def TryRunQuery(self):
		try:
			result = self.__cursor.execute(self.query)

		except Exception as e:
			print(f"Executing query has failed:\n{e}")
			return False

		return True

	def Commit(self):
		self.__db.commit()

	def DisplaySelected(self):
		try:
			result = self.__cursor.fetchall()
			self.QueryResultToPandas(result)
			print("")
			print(self.__dataframe)

		except Exception as e:
			print(f"Displaying select query has failed:\n{e}")

	def ExportToExcel(self, outputFile, sql_query):
		outputFile = self.__parent_dir / outputFile
		try:
			result = self.__cursor.execute(sql_query).fetchall()
		except Exception as e:
			print(f"Executing fetch all data from table has failed:\n{e}")
			sys.exit(1)

		self.QueryResultToPandas(result)
		self.__dataframe.to_excel(outputFile, index=False)

#initialize
database = Database(databaseFile)
