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

current_directory= os.getcwd() # this may change before beta/alpha testing.

if __name__ == '__main__':
    print('testing ffe validation')
    # print(db.check_odbc())
    print(current_directory)
    print(ffe_val.db_store)

    os.system("pause")
