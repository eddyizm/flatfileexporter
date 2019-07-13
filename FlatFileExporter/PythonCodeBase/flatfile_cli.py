''' Testing python script to be called from WPF C# applicaiton.
    Compiling with pyinstaller to EXE.
    pyinstaller -F --icon="../ffe.ico" --clean --distpath "../Resources" flatfile_cli.py
    
'''
import os
import DAL as db # local library
import ffe_validation as ffe_val # Local Library
import argparse
import sys

if __name__ == '__main__':
    print('hello world')
    os.system("pause")