#!/usr/bin/env python3

from account import Account

import string
import random

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

def check_existing_accounts(username):
  '''
  Function that check if an account exists with that username and return a Boolean
  '''
  return Account.account_exist(username)


def find_account(username):
  '''
  Function that finds a contact by number and returns the contact
  '''
  return Account.find_by_username(username)



S = 12  # number of characters in the random password.  
# call random.choices() string module to find the string in Uppercase + numeric data.  
ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))


def main():
  print("Hello Welcome to your credentials list. What is your name?")
  user_name = input()

  print(f"Hello {user_name}. What would you like to do?")
  print('\n')

  while True:
    print("Use these short codes : ca - create a new account, da - display accounts, de -delete an account, ex -exit the account list")

    short_code = input().lower()

    if short_code == 'ca':
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

    elif short_code == 'da':
      if display_accounts():
        print("Here is a list of all your accounts")
        print("\n")

        for account in display_accounts():
          print(f"username: {account.user_name} | password: {account.password}")
        
        print('\n')
      else:
        print('\n')
        print("You dont seem to have any contacts saved yet")
        print('\n')
    
    elif short_code == 'de':
      print("Enter the username of the account you want to delete")

      search_username = input()
      if check_existing_accounts(username):
        search_account = find_account(username)
        delete_account(search_account)
      else:
        print("That contact does not exist")
    
    elif short_code == 'ex':
      print("Bye .......")
      break


if __name__ == '__main__':
  main()