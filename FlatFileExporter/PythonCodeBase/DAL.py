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
# TODO figure out how to auto increment this and pass it/share it with c# codebase
__version__= '0.0.1.0' 

DB_STRING = 'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={};Trusted_Connection=yes;DATABASE={}'	
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
    print(f'error in check_odbc(): {ex}')


def read_file(file):
  ''' method to read sql script. 
  TODO Will add a check to validate that it has
  SET NO COUNT in it '''
  try:
    with open(file, 'r') as f:
      _qry = f.read()
      return _qry
  except Exception as ex:
    print(f'error in read_file(): {ex}')


def generate_file(query, db_name, server, separator, directory, extension, file_name=None, username=None, password=None):
  # defaulting to no username and going to trusted connection. Should be the setup in most enterprise shops
  if not username:
    db_connection=DB_STRING.format(server, db_name)
  else:
    db_connection = USERPASS_DBSTRING.format(server, db_name, username, password)
  # passing the name supplied otherwise defaulting but this may not work properly. Need to test in other environments.
  if file_name:
    filename = (file_name+'_'+date_var+extension)
  else:
    filename = os.path.join(directory, (f'ffe_output_{date_var}{extension}'))
  # connect to db and execute query, output file
  try:
    with db.connect(db_connection) as cnxn:
        df = pd.read_sql((query), cnxn)
        if extension == '.xlsx':
          writer = pd.ExcelWriter(filename, engine = 'xlsxwriter')
          df.to_excel(writer, sheet_name = (db_name), index = False)
        else:
          df.to_csv(filename ,sep = separator, encoding='utf-8', index = False)
    return filename
  except Exception as ex:
    print(f'error in generate_file() function: {ex}')
  

if __name__ == '__main__':
  # main()
  pass
  # TODO Add version 
  # TODO Add logging
  
  
  
