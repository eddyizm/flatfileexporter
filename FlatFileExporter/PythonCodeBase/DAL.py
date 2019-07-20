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
__version__= '0.0.0.2' 

DB_STRING = 'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={};Trusted_Connection=yes;DATABASE={}'	
ODBC_MISSING_MSG = '''ODBC driver not found
please install ODBC Driver 17 for SQL Server
https://www.microsoft.com/en-us/download/details.aspx?id=56567'''

def check_odbc() -> bool:
  try:
    drivers = db.drivers()
    if drivers:
      print('checking for \'ODBC Driver 17 for SQL Server\' driver')
      for driver in drivers:
        if driver== 'ODBC Driver 17 for SQL Server':
          return True
      else:
        print(ODBC_MISSING_MSG)
        return False    
    else:
      print(ODBC_MISSING_MSG)
      return False
  except Exception as ex:
    print (ex)    


def read_file(file):
  ''' method to read sql script. 
  Will add a check to validate that it has
  SET NO COUNT in it '''
  try:
    with open(file, 'r') as f:
      _qry = f.read()
      return _qry
  except Exception as ex:
    print (ex)


def generate_file(query, db_name, server, seperator, extension, file_name=None):
  db_connection = DB_STRING.format(server, db_name)
  # testing db connection
  print(db_connection)
  


if __name__ == '__main__':
  # main()
  pass
  # TODO Add version 
  # TODO Add logging
  
  
  
