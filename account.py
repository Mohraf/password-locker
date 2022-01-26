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
    save_contact method saves contact objects into contact_list
    '''

    Account.account_list.append(self)