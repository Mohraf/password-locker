import string    
import random # define the random module  

class User:
  '''
  class that generates new instance of a user
  '''

  users_list =[]
  S = 12  # number of characters in the random password.  
  # call random.choices() string module to find the string in Uppercase + numeric data.  
  ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = S))

  def __init__(self, user_name, password):
    self.user_name = user_name
    self.password = password
  

  def create_new_insta_user(self):
    User.users_list.append(self)
