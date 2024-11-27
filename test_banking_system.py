# test_banking_system.py
import unittest
from banking_system import deposit, withdraw, transfer, add_account, find_account, display_all_accounts

class TestBankingSystem(unittest.TestCase):

    def setUp(self):
        self.accounts = {
            'John': {'balance': 1000},
            'Jane': {'balance': 500}
        }

    def test_deposit(self):
        deposit(self.accounts['John'], 200)
        self.assertEqual(self.accounts['John']['balance'], 1200)

    def test_withdraw(self):
        withdraw(self.accounts['John'], 500)
        self.assertEqual(self.accounts['John']['balance'], 700)
        withdraw(self.accounts['John'], 1000)
        self.assertEqual(self.accounts['John']['balance'], 700)  # Insufficient funds

    def test_transfer(self):
        transfer(self.accounts['John'], self.accounts['Jane'], 300)
        self.assertEqual(self.accounts['John']['balance'], 400)
        self.assertEqual(self.accounts['Jane']['balance'], 800)
        transfer(self.accounts['John'], self.accounts['Jane'], 500)
        self.assertEqual(self.accounts['John']['balance'], 400)  # Insufficient funds

    def test_add_account(self):
        add_account(self.accounts, 'Alice', 100)
        self.assertIn('Alice', self.accounts)
        self.assertEqual(self.accounts['Alice']['balance'], 100)
        add_account(self.accounts, 'Alice', 200)  # Trying to add the same account
        self.assertEqual(self.accounts['Alice']['balance'], 100)  # Account still has initial balance

    def test_find_account(self):
        self.assertEqual(find_account(self.accounts, 'Jane'), {'balance': 500})
        self.assertIsNone(find_account(self.accounts, 'Bob'))  # Account doesn't exist

    def test_display_all_accounts(self):
        result = display_all_accounts(self.accounts)
        self.assertIn('John: 1000', result)
        self.assertIn('Jane: 500', result)

if __name__ == "__main__":
    unittest.main()
