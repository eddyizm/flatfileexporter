''' Data Access Layer
Main library to access database, read sql scripts, and generate files. 
Will also use this area to check for ODBC.
'''
import pyodbc as db
import pandas as pd
import os
import sys
from datetime import datetime
import xlsxwriter
import logging
from flatfileexporter.models.data_service import DatabaseConnectionTest
log = logging.getLogger('root')

date_var = datetime.now().strftime("%Y%m%d")
# When called from UI the directory will default to the location of the SQL script. 

DB_STRING = 'DRIVER={{{}}};SERVER={};Trusted_Connection=yes;DATABASE={}'
USERPASS_DBSTRING = 'DRIVER={{{}}};SERVER={};DATABASE={};UID={};PWD={}'
ODBC_MISSING_MSG = '''ODBC driver not found
please install ODBC Driver for SQL Server
https://learn.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver16'''
MSDRIVERS = ['ODBC Driver 18 for SQL Server', 'ODBC Driver 17 for SQL Server', 'SQL Server Native Client 11.0', 'SQL Server']


def get_os_and_platform() -> tuple:
    return (sys.platform, os.system('uname -a'))


def test_db_connect(params) -> DatabaseConnectionTest:
    params.get('db_type')
    params.get('database')
    params.get('server')
    db_connection = DB_STRING.format(MSDRIVERS[0], params.get('server'), params.get('database'))
    db_result = DatabaseConnectionTest(
        message='',
        success_response=False
    )
    try:
        conn = db.connect(db_connection)
        conn.close()
        db_result.message = f"Connected to {params.get('server')}"
        return db_result
    except db.Error as e:
        # print("Error connecting to SQL Server:", e)
        db_result.message = f"Unable connect to Server: {e}"
        return db_result


def check_odbc(params, platform) -> bool:
    ''' check for odbc driver on nt systems.'''
    try:
        drivers = db.drivers()
        if platform == 'linux':
            return test_db_connect(params, drivers)
        log.info(os.system('uname -a'))
        if drivers:
            log.info('Checking for a compatible driver')
            for driver in MSDRIVERS:
                if driver in drivers:
                    log.info(f'Driver found - {driver}')
                    return True
                else:
                    log.warning(ODBC_MISSING_MSG)
                    return False
        else:
            log.warning(ODBC_MISSING_MSG)
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
    log.error(f'Error in generate_file() function: {ex}')
  

if __name__ == '__main__':
  
  pass
  # TODO Add version 
