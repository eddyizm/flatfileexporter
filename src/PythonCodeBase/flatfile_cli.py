''' Python script to be called from WPF C# applicaiton.
    Compiling with pyinstaller to EXE.
    pyinstaller -F --icon="../ffe.ico" --clean --version-file=flatfile_cli.txt --distpath "../Resources" flatfile_cli.py
    
    # testing environment
    # linux sql server - 127.0.0.1,14333
    # database - TutorialDB
   
''' 
import os
import DAL as db # local library
import argparse
import logging
from logging.handlers import RotatingFileHandler
import sys
directory = os.getcwd() 

LOG_DIR = directory
LOG_FILE = os.path.join(LOG_DIR, 'flatfile_cli.log') 
FINISH_MSG = 'Closing FFE CLI'
log_formatter = logging.Formatter('%(asctime)s | %(levelname)s | %(message)s')
log_handler = RotatingFileHandler(LOG_FILE, mode='a', maxBytes=5*1024*1024, 
                                 backupCount=5, encoding=None, delay=0)
log_handler.setFormatter(log_formatter)
log = logging.getLogger('root')
log.setLevel(logging.DEBUG)
log.addHandler(log_handler)
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
ch.setFormatter(log_formatter)
log.addHandler(ch)


# argument parser
parser = argparse.ArgumentParser(description="Reads a sql script or calls a stored procedure and exports results to a csv, txt or excel file.")
parser.add_argument("-V", "--version", action='version', version =f'{db.__version__}')
parser.add_argument("server", help="server to run query against.")
parser.add_argument("db", help="database to use on server.")
parser.add_argument("directory", help="location to export flat file. do not specify extension.")
# optionals
parser.add_argument("-f", "--filename", help="filename. Date will be appended.", required=False)
parser.add_argument("-u", "--username", help="username for db connection.", default=None, required=False)
parser.add_argument("-pass", "--password", help="use login/pass from instead of default Integrated Security (Trusted_Connection).", default=None, required=False)
# real first group for extension
group_extension = parser.add_mutually_exclusive_group(required=True)
group_extension.add_argument("-csv", "--csv", action='store_const', const='.csv', help="output file with csv extension.")
group_extension.add_argument("-txt", "--txt", action='store_const', const='.txt', help="output file with txt extension.")
group_extension.add_argument("-xlsx", "--xlsx", action='store_const', const='.xlsx', help="output excel file.")
# first group for seperator
group_seperator = parser.add_mutually_exclusive_group(required=True)
group_seperator.add_argument("-c", "--comma", action='store_const', const=',', help="use comma character for seperator.")
group_seperator.add_argument("-t", "--tab", action='store_const', const='\t', help="use tab for seperator.")
group_seperator.add_argument("-p", "--pipe", action='store_const', const='|', help="use pipe character for seperator.")
# second group for sql script or stored proc
group_sql = parser.add_mutually_exclusive_group(required=True)
group_sql.add_argument("-s", "--sqlscript",  help="full path of sql script *MUST HAVE* SET NO COUNT on script.")
group_sql.add_argument("-sp", "--storedproc", help="instead of sql script, point to stored procedure on database. Wrap in double quotes with parameters eg. \"EXEC SAMPLE_SP '<Param>'\"")

args=parser.parse_args()
current_directory= os.getcwd() # this may change before beta/alpha testing.

def clean_path(dir_path):
    return dir_path.replace('\\', '/')


def get_seperator():
    ''' find argument with value from GUI or CLI '''
    # TODO test against DB. the \t might work directly from the constant
    log.info('Getting separator...')
    if args.comma:
        return args.comma
    elif args.tab:
        return args.tab
    else:
        return args.pipe    


def get_extension():
    ''' find extension with value from GUI or CLI '''
    # TODO test against DB. the \t might work directly from the constant
    log.info('Getting extenstion...')
    if args.csv:
        return args.csv
    elif args.txt:
        return args.txt
    else:
        return args.xlsx        


def log_args():
    ''' CLI arg inputs -debugging method only'''
    log.debug(f'args.server: {args.server}')
    log.debug(f'args.db: {args.db}')
    log.debug(f'args.directory: {args.directory}')
    log.debug(f'args.filename: {args.filename}')
    log.debug(f'args.comma: {args.comma}')
    log.debug(f'args.tab: {args.tab}')
    log.debug(f'args.pipe: {args.pipe}')
    log.debug(f'args.sqlscript: {args.sqlscript}')
    log.debug(f'args.storedproc: {args.storedproc}')
    log.debug(f'args.username: {args.username}')
    log.debug(f'args.password: {args.password}')
    

def get_login():
    ''' assign login credentials if passed from GUI or from CLI '''
    if args.username:
        log.debug('Getting credentials')
        return args.username, args.password
    else:
        log.debug('no credentials found, returning None')
        return None, None        


def get_filename():
    pass
    # TODO pass filename or generate default here if none is pass
    # since i didn't fucking make it required in the args. DUMB DUMB!

def main():
    # odbc check
    if not db.check_odbc():
        log.warn("Try again after installing ODBC driver. Application exiting.")
        os.system("pause")
        sys.exit()
    
    login, cred = get_login()
    
    try:
        if not args.sqlscript:
            ''' if sql script is None/null then process using stored proc '''
            log.info(f'executing stored proc {args.storedproc}') 
            # fullpath = os.path.join(args.directory, args.filename)
            result = db.generate_file(args.storedproc, args.db, args.server, get_seperator(), args.directory, get_extension(), username=login, password=cred)
        else:
            log.info(f'executing sql script {args.sqlscript}')
            qry = db.read_file(args.sqlscript)
            
            result = db.generate_file(qry, args.db, args.server, get_seperator(), clean_path(args.directory), get_extension(), username=login, password=cred)
    except Exception as ex:
        log.error(f'error in main(): {ex}')
    finally: 
        if result:
            log.info(f'file generated - {result}')
        else:
            log.info(f'No file generated. Please check the logs')
        os.system("pause")      
    

if __name__ == '__main__':
    log.info(f'Startiing FFE CLI version: {db.__version__}')
    # log_args()
    main()
    log.info(FINISH_MSG)
    
