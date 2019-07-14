''' Testing python script to be called from WPF C# applicaiton.
    Compiling with pyinstaller to EXE.
    pyinstaller -F --icon="../ffe.ico" --clean --distpath "../Resources" flatfile_cli.py
    
'''
import os
import DAL as db # local library
import ffe_validation as ffe_val # Local Library
import argparse
import sys

current_directory= os.getcwd() # this may change before beta/alpha testing.

if __name__ == '__main__':
    print('testing ffe validation')
    # print(db.check_odbc())
    print(current_directory)
    print(ffe_val.db_store)

    os.system("pause")
