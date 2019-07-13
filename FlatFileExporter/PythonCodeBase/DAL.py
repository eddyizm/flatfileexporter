''' Data Access Layer
Main library to access database, read sql scripts, and generate files. 
Will also use this area to check for ODBC.
'''
import pyodbc as db
import pandas as pd
import os
from datetime import datetime
date_var = datetime.now().strftime("%Y%m%d")
# TODO When called from UI the directory will default to the location of the SQL script. 
directory = '' 
# TODO figure out how to auto increment this and pass it/share it with c# codebase
__version__= '0.0.0.1' 

DB_STRING = 'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={};Trusted_Connection=yes;DATABASE={}'	

# TODO check for ODBC drivers
def check_odbc() -> bool:
  return True



if __name__ == '__main__':
  main()
  # TODO Add version 
  # TODO Add logging
  
  
  
