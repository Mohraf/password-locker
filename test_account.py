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

