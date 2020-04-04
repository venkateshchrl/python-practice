from unittest.mock import patch
import unittest, UserManagementSystem
import logging

class TestUserManagementSystem(unittest.TestCase):
    logging.basicConfig(filename="C:\\Venkatesh\\Work\\Repos\\python-practice\\exercises\\User Registration\\logs\\ums_app.log",
                            level = logging.DEBUG)
    logger = logging.getLogger("TestUserManagementSystem")

    def test_user_account_creation_with_valid_values(self):
        user_input = [
            'Venkatesh M',
            '26',
            '989989887',
            'venkatesh@gmail.com',
            'venkatesh.m',
            '2'
        ]
        
        ums = UserManagementSystem.UserManagementSystem()
        with patch('builtins.input', side_effect=user_input):
            userAccount = ums.addUser()
        self.logger.debug("User Account Details: {ua}".format(ua=userAccount.toDictObject()))
        self.assertNotEqual(userAccount, None)

    def test_user_account_creation_with_invalid_values(self):
        user_input = [
            'Venkatesh M',
            'test',
            '989989887',
            'venkatesh@gmail.com',
            'venkatesh.m',
            '2'
        ]

        ums = UserManagementSystem.UserManagementSystem()
        with patch('builtins.input', side_effect=user_input):
            userAccount = ums.addUser()
        self.logger.debug("User Account Details: {ua}".format(ua=userAccount.toDictObject()))
        self.assertNotEqual(userAccount, None)