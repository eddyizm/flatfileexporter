''' library to build validation for trail period and possibly licensing. 
will use this to build sqlite db and encrypt for usage in c# portion
'''
import requests
import os
import sqlite3
from datetime import datetime, timedelta
db_store='file.sqlite3'
current_directory = os.getcwd()
dateTimeStart = datetime(2020, 8, 1)



def check_url():
    r = requests.get('https://storage.cloud.google.com/som_eddyizm/TWC.png')
    # print(r.status_code)
    # print('true' if r.status_code==200 else 'false')
    return True if r.status_code==200 else False


# TODO Get current date and store in sqlite3 for 30 day trial. 
''' sqlite3 statements '''
create_validation_table = """ CREATE TABLE IF NOT EXISTS validation_date (
                                        id integer PRIMARY KEY,
                                        current_date text,
                                        start_date text
                                    ); """		


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)
    return None  

# check if db exists
def check_if_file_exists(full_filepath) -> bool:
  return os.path.exists(full_filepath)


def check_date():
    time_between_insertion = datetime.now() - dateTimeStart
    if  time_between_insertion.days > 90:
        return False
    else:
        return True


def validate():
    if check_url() and check_date():
         return True
         # if check_date():
    else:
        return False

 

if __name__ == '__main__':
    pass
    
    
    
    
  