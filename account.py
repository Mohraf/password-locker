class Account:
  '''
  class that generates new instance of an account
  '''
  account_list = []
  def __init__(self, user_name, password):
    self.user_name = user_name
    self.password = password
  

  def save_account(self):
    '''
    save_account method saves account objects into account_list
    '''

    Account.account_list.append(self)

  
  def delete_account(self):
    '''
    delete_account method deletes a saved account from the account_list
    '''

    Account.account_list.remove(self)


  @classmethod
  def display_accounts(cls):
    '''
    method that returns the account list
    '''
    return cls.account_list


  @classmethod
  def find_by_username(cls,username):
    '''
    Method that takes in a username and returns an account that matches that number.

    Args:
        username: username to search for
    Returns :
        Account that matches the username.
    '''

    for account in cls.account_list:
      if account.user_name == username:
        return account
  

  @classmethod
  def account_exist(cls,username):
    '''
    Method that checks if an account exists from the account list.
    Args:
        username: Username to search if it exists
    Returns :
        Boolean: True or false depending if the account exists
    '''
    for account in cls.account_list:
        if account.user_name == username:
                return True

    return False
  