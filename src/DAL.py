''' Data Access Layer
Main library to access database, read sql scripts, and generate files. 
Will also use this area to check for ODBC.
'''
import pyodbc as db
import pandas as pd
import os
from datetime import datetime
# import xlsxwriter
import logging
log = logging.getLogger('root')

date_var = datetime.now().strftime("%Y%m%d")
# When called from UI the directory will default to the l`ocation of the SQL script. 
# TODO figure out how to auto increment this and pass it/share it with c# codebase
__version__= '0.1.5'

DB_STRING = 'DRIVER={{{}}};SERVER={};Trusted_Connection=yes;DATABASE={}'	
USERPASS_DBSTRING = 'DRIVER={{{}}};SERVER={};DATABASE={};UID={};PWD={}'
ODBC_MISSING_MSG = '''ODBC driver not found
please install ODBC Driver 17 for SQL Server
https://www.microsoft.com/en-us/download/details.aspx?id=56567'''
MSDRIVERS = ['ODBC Driver 17 for SQL Server', 'ODBC Driver 13 for SQL Server',
   'SQL Server Native Client 11.0', 'SQL Server']


def check_odbc() -> bool:
  ''' check for odbc driver '''
  try:
    drivers = db.drivers()
    if drivers:
      log.info('Checking for \'ODBC Driver 17 for SQL Server\' driver')
      for driver in drivers:
        if driver == 'ODBC Driver 17 for SQL Server':
            log.info(f'Driver found - {driver}')
            return True
        if driver == 'ODBC Driver 11 for SQL Server':
            log.info(f'Driver found - {driver}')
            return True
      else:
        log.warn(ODBC_MISSING_MSG)
        return False    
    else:
      log.warn(ODBC_MISSING_MSG)
      return False
  except Exception as ex:
    log.error(f'Error in check_odbc(): {ex}')


def get_odbc() -> str:
  ''' get odbc driver - the check should have already been done and pass
  however maybe I need to combine this later to specify which one to use.
  '''
  try:
    drivers = db.drivers()
    if drivers:
      log.info('Loading driver')
      for driver in MSDRIVERS:
        if driver in drivers:
          log.info(f'Driver found - {driver}')
          return driver

  except Exception as ex:
    log.error(f'Error in get_odbc(): {ex}')


def read_file(file):
  ''' method to read sql script. 
  TODO Will add a check to validate that it has
  SET NO COUNT in it '''
  try:
    log.info('Reading sql script from file.')
    with open(file, 'r') as f:
      _qry = f.read()
      return _qry
  except Exception as ex:
    log.error(f'Error in read_file(): {ex}')
    

def generate_file(query, db_name, server, separator, directory, extension, file_name=None, username=None, password=None):
  ''' generate file magic '''
  log.info('Generating file')
  driver = get_odbc()
  # defaulting to no username and going to trusted connection. Should be the setup in most enterprise shops
  if not username:
    log.debug('No username received, using trusted connection (MSSQL)')
    db_connection=DB_STRING.format(driver, server, db_name)
  else:
    db_connection = USERPASS_DBSTRING.format(driver, server, db_name, username, password)
  # passing the name supplied otherwise defaulting but this may not work properly. Need to test in other environments.
  if file_name:
    filename = (file_name + '_' + date_var + extension)
  else:
    filename = os.path.join(directory, (f'ffe_output_{date_var}{extension}'))
  # connect to db and execute query, output file
  try:
    log.info('Connecting to database server')
    log.debug(f'DB_STRING: {db_connection}')
    with db.connect(db_connection) as cnxn:
        df = pd.read_sql((query), cnxn)
        if extension == '.xlsx':
          writer = pd.ExcelWriter(filename, engine = 'xlsxwriter')
          df.to_excel(writer, sheet_name = (db_name), index = False)
          writer.save()
          writer.close()
        else:
          df.to_csv(filename ,sep = separator, encoding='utf-8', index = False)
    return filename
  except Exception as ex:
    # print(f'error in generate_file() function: {ex}')
    log.error(f'Error in generate_file() function: {ex}')
  

if __name__ == '__main__':
  check_odbc()
  pass
  # TODO Add version 
  
  
  
