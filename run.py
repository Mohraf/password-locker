#!/usr/bin/env python3

from account import Account

def create_account(uname,password):
  '''
  Function to create a new account credentials
  '''
  new_account = Account(uname,password)
  return new_account


def save_accounts(account):
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


def main():
  print("Hello Welcome to your credentials list. What is your name?")
  user_name = input()

  print(f"Hello {user_name}. What would you like to do?")
  print('\n')

  while True:
    print("Use these short codes : cc - create a new account, dc - display accounts, fc -find an account, ex -exit the account list")

    short_code = input().lower()

    if short_code == 'cc':
      print("New Account")
      print("-"*10)

      print("Username ....")
      username = input()

      print("Password ....")
      password = input()

      save_accounts(create_account(username, password))
      print('\n')
      print(f"New Account {username} with password: {password} created")
      print('\n')

    
    elif short_code == 'ex':
      print("Bye .......")
      break


if __name__ == '__main__':
  main()