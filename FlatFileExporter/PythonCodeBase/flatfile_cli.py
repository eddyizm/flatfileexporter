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
parser.add_argument("server", help="server to run query against")
parser.add_argument("db", help="database to use on server")
parser.add_argument("directory", help="location to export flat file. do not specify extension.")
parser.add_argument("filename", help="filename. date will be appended")
args=parser.parse_args()

current_directory= os.getcwd() # this may change before beta/alpha testing.

def get_seperator(*, seperator):
    ''' get file seperator from GUI or CLI and pass the correct value to function '''
    pass

def main():
    # debugging CLI arg inputs
    print(args.server)
    print(args.db)
    print(args.directory)
    print(args.filename)

if __name__ == '__main__':
    main()
    # print('testing check odbc')
    # print(db.check_odbc())
    # print('testing ffe validation')
    # print(current_directory)
    # print(ffe_val.db_store)

    os.system("pause")
    
