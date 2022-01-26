import unittest
from account import Account

class TestAccount(unittest.TestCase):
  '''
    Test class that defines test cases for the contact class behaviours.

    Args:
        unittest.TestCase: TestCase class that helps in creating test cases
  '''
  def setUp(self):
    '''
    Set up method to run before each test cases.
    '''
    self.new_account = Account("mohraf","Denime123") # create account object
  
  # def tearDown(self):
  #   '''
  #   tearDown method that does clean up after each test case has run.
  #   '''
  #   Contact.contact_list = []


  def test_init(self):
    '''
    test_init test case to test if the object is initialized properly
    '''

    self.assertEqual(self.new_account.user_name,"mohraf")
    self.assertEqual(self.new_account.password,"Denime123")
  

  def test_save_account(self):
    '''
    test_save_contact test case to test if the contact object is saved into
      the contact list
    '''
    self.new_account.save_account() # saving the new contact
    self.assertEqual(len(Account.account_list),1)


if __name__ == '__main__':
  unittest.main()
