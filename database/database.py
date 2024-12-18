import sys
import sqlite3
from pathlib import Path

class Database():
	def __init__(self, databaseFile):
		#move to root folder, then add the file location
		self.__parent_dir = Path(__file__).parent.parent.absolute()
		databaseFile = self.__parent_dir / databaseFile

		#make connection
		try:
			self.__database = sqlite3.connect(databaseFile)
			self.__cursor = self.__database.cursor()
		except Exception as e:
			print(f"Connecting to database failed")
			print(e)
			sys.exit(1)

	def ExportMembers(self, outputFile):
		sys.exit(0)

