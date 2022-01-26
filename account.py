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
