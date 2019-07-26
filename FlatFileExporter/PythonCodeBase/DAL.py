''' Data Access Layer
Main library to access database, read sql scripts, and generate files. 
Will also use this area to check for ODBC.
'''
import pyodbc as db
import pandas as pd
import os
from datetime import datetime
import xlsxwriter
date_var = datetime.now().strftime("%Y%m%d")
# TODO When called from UI the directory will default to the location of the SQL script. 
directory = os.getcwd() 
# TODO figure out how to auto increment this and pass it/share it with c# codebase
__version__= '0.0.0.2' 

# DB_STRING = 'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={};Trusted_Connection=yes;DATABASE={}'	
DB_STRING = 'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={};DATABASE={};UID=sa;PWD=ex0Planet693$'	
USERPASS_DBSTRING = 'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={};DATABASE={};UID={};PWD={}'
ODBC_MISSING_MSG = '''ODBC driver not found
please install ODBC Driver 17 for SQL Server
https://www.microsoft.com/en-us/download/details.aspx?id=56567'''

def check_odbc() -> bool:
  try:
    drivers = db.drivers()
    if drivers:
      print('checking for \'ODBC Driver 17 for SQL Server\' driver')
      for driver in drivers:
        if driver == 'ODBC Driver 17 for SQL Server':
          print('Driver found')
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


def generate_file(query, db_name, server, separator, extension, file_name=None):
  db_connection = DB_STRING.format(server, db_name)
  # testing db connection
  print(db_connection)
  # print(extension)
  if file_name:
    filename = (file_name+'_'+date_var+extension)
  else:
    filename = os.path.join(directory, (f'ffe_output_{date_var}{extension}'))
  
  try:
    with db.connect(db_connection) as cnxn:
        print(cnxn)
        df = pd.read_sql((query), cnxn)
        print('in using')
        if extension == '.xlsx':
          writer = pd.ExcelWriter(filename, engine = 'xlsxwriter')
          df.to_excel(writer, sheet_name = (db_name), index=False)
        else:
          df.to_csv(filename ,sep = separator, encoding='utf-8', index = False)
    return filename
  except Exception as ex:
    return print(ex)
  else:
    print(f'file generated - {result}')
  

if __name__ == '__main__':
  # main()
  pass
  # TODO Add version 
  # TODO Add logging
  
  
  
