''' Testing python script to be called from WPF C# applicaiton.
    Compiling with pyinstaller to EXE.
    pyinstaller -F --icon="../ffe.ico" --clean --distpath "../Resources" flatfile_cli.py
    
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
parser.add_argument("filename", help="filename. Date will be appended/")
# first group for extension
group_seperator = parser.add_mutually_exclusive_group(required=True)
group_seperator.add_argument("-c", "--comma", action='store_const', const=',', help="use comma characterfor seperator.")
group_seperator.add_argument("-t", "--tab", action='store_const', const='t', help="uses tab for seperator.")
group_seperator.add_argument("-p", "--pipe", action='store_const', const='|', help="uses pipe character for seperator.")
# second group for sql script or stored proc
group_sql = parser.add_mutually_exclusive_group(required=True)
group_sql.add_argument("-s", "--sqlscript",  help="full path of sql script *MUST HAVE* SET NO COUNT on script.")
group_sql.add_argument("-sp", "--storedproc", help="instead of sql script, point to stored procedure on database. Wrap in double quotes with parameters eg. \"EXEC SAMPLE_SP '<Param>'\"")

args=parser.parse_args()

current_directory= os.getcwd() # this may change before beta/alpha testing.

def get_seperator(*, seperator):
    ''' get file seperator from GUI or CLI and pass the correct value to function '''
    # TODO test against DB. the \t might work directly from the constant
    pass

def main():
    # debugging CLI arg inputs
    print(args.server)
    print(args.db)
    print(args.directory)
    print(args.filename)
    print(args.comma)
    print(args.tab)
    print(args.pipe)

if __name__ == '__main__':
    main()
    # print('testing check odbc')
    # print(db.check_odbc())
    # print('testing ffe validation')
    # print(current_directory)
    # print(ffe_val.db_store)

    os.system("pause")
