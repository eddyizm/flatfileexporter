''' library to build validation for trail period and possibly licensing. 
will use this to build sqlite db and encrypt for usage in c# portion
'''
import requests
import os
import sqlite3

# link to check https://www.instagram.com/p/voLqUzoTVk/?igshid=6astge42ug6y

def check_url():
  r = requests.get('https://www.instagram.com/p/voLqUzoTVk/')
  # print(r.status_code)
  # print('true' if r.status_code==200 else 'false')
  return True if r.status_code==200 else False

if __name__ == '__main__':
  # pass
  print(check_url())