''' Testing python script to be called from WPF C# applicaiton.
    Compiling with pyinstaller to EXE.
    pyinstaller -F --icon="../ffe.ico" --clean --distpath "../Resources" flatfile_cli.py
    
    # testing environment
    # linux sql server - 127.0.0.1,14333
    # database - TutorialDB
    
''' 
import os
import DAL as db # local library
import ffe_validation as ffe_val # Local Library
import argparse
import sys

# argument parser
parser = argparse.ArgumentParser(description="Takes sql script or stored proc to export csv, txt or excel file.")
parser.add_argument("-V", "--version", action='version', version =f'v{db.__version__}')
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
group_seperator.add_argument("-t", "--tab", action='store_const', const='\t', help="uses tab for seperator.")
group_seperator.add_argument("-p", "--pipe", action='store_const', const='|', help="uses pipe character for seperator.")
# second group for sql script or stored proc
group_sql = parser.add_mutually_exclusive_group(required=True)
group_sql.add_argument("-s", "--sqlscript",  help="full path of sql script *MUST HAVE* SET NO COUNT on script.")
group_sql.add_argument("-sp", "--storedproc", help="instead of sql script, point to stored procedure on database. Wrap in double quotes with parameters eg. \"EXEC SAMPLE_SP '<Param>'\"")

args=parser.parse_args()
current_directory= os.getcwd() # this may change before beta/alpha testing.

def get_seperator():
    ''' find argument with value from GUI or CLI '''
    # TODO test against DB. the \t might work directly from the constant
    if args.comma:
        return args.comma
    elif args.tab:
        return args.tab
    else:
        return args.pipe    


def get_extension():
    ''' find extension with value from GUI or CLI '''
    # TODO test against DB. the \t might work directly from the constant
    if args.csv:
        return args.csv
    elif args.txt:
        return args.txt
    else:
        return args.xlsx        

# debugging method
def print_args():
    # CLI arg inputs
    print(args.server)
    print(args.db)
    print(args.directory)
    print(args.filename)
    print(args.comma)
    print(args.tab)
    print(args.pipe)
    print(args.sqlscript)
    print(args.storedproc)
    print(args.username)
    print(args.password)
    # print('testing check odbc')
    # print(db.check_odbc())
    # print('testing ffe validation')
    # print(current_directory)
    # print(ffe_val.db_store)


def get_login():
    ''' assign login credentials if passed from GUI or from CLI '''
    if args.username:
        return args.username, args.password
    else:
        return None, None        


def main():
    # odbc check
    if not db.check_odbc():
        print("Try again after installing ODBC driver. Application exiting.")
        os.system("pause")
        sys.exit()
    if not ffe_val.validate():
        print("Trial is over. Please buy a license.")
        os.system("pause")
        sys.exit()
    
    login, cred = get_login()

    try:
        if not args.sqlscript:
            ''' if sql script is None/null then process using stored proc '''
            print (f'executing stored proc {args.storedproc}') 
            fullpath = os.path.join(args.directory, args.filename)
            result = db.generate_file(qry, args.db, args.server, get_seperator(), get_extension(), fullpath, login, cred)
        else:
            print (f'executing sql script {args.sqlscript}')
            qry = db.read_file(args.sqlscript)
            fullpath = os.path.join(args.directory, args.filename)
            result = db.generate_file(qry, args.db, args.server, get_seperator(), get_extension(), fullpath, login, cred)
    except Exception as ex:
        print(f'error in main(): {ex}')
    else: 
      print(f'file generated - {result}')        
    

if __name__ == '__main__':
    main()
    os.system("pause")
