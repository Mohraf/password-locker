#!/usr/bin/env python3

from account import Account

def create_account(uname,password):
  '''
  Function to create a new account credentials
  '''
  new_account = Account(uname,password)
  return new_account


def save_account(account):
  '''
  Function to save account
  '''
  account.save_account()


def delete_account(account):
  '''
  Function to delete account
  '''
  account.delete_account()


def display_accounts():
  '''
  Function to return all saved accounts
  '''
  return Account.display_accounts()