from models.account import Account
from app import mongodb


class Savings(Account):
    def __init__(
        self, name, emailID, balance, pin_number, privilege, date_of_birth, gender, age
    ):
        super().__init__(name, balance, pin_number, privilege, emailID)
        self.gender = gender
        self.date_of_birth = date_of_birth
        self.age = age

    def store_in_mongodb(self):
        super().store_in_mongodb("savings")
        mongodb.SavingsAccounts.insert_one(
            {
                "Account_Number": self.account_number,
                "Date_of_birth": str(self.date_of_birth),
                "Gender": self.gender,
                "Age": self.age,
            }
        )
        return True
