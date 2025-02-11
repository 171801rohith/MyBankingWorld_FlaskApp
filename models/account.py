from datetime import datetime
from repositories.account_repository import AccountRepository
from werkzeug.security import generate_password_hash
from app import mongodb


class Account:
    def __init__(self, name, balance, pin_number, privilege, emailID):
        self.account_number = AccountRepository.generate_account_number()
        self.name = name
        self.emailID = emailID
        self.pin_number = pin_number
        self.balance = balance
        self.privilege = privilege
        self.is_active = True
        self.open_date = datetime.now()
        self.close_date = None

    def store_in_mongodb(self, type):
        mongodb.Accounts.insert_one(
            {
                "Account_Number": self.account_number,
                "Account_type": type,
                "Name": self.name,
                "EmailID": self.emailID,
                "Pin_Number": generate_password_hash(self.pin_number),
                "Balance": self.balance,
                "Privilege": self.privilege,
                "Activity": self.is_active,
                "Open_date": str(self.open_date),
                "Close_date": self.close_date,
            }
        )
