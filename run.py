#!/usr/bin/env python3

from account import Account

def create_account(uname,password):
  '''
  Function to create a new account credentials
  '''
  new_account = Account(uname,password)
  return new_account
