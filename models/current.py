from models.account import Account
from app import mongodb


class Current(Account):
    def __init__(
        self,
        name,
        emailID,
        balance,
        pin_number,
        privilege,
        registration_number,
        website_url,
    ):
        super().__init__(name, balance, pin_number, privilege, emailID)
        self.registration_number = registration_number
        self.website_url = website_url

    def store_in_mongodb(self):
        super().store_in_mongodb("current")
        mongodb.SavingsAccounts.insert_one(
            {
                "Account_Number": self.account_number,
                "Registration_number": self.registration_number,
                "Website_URL": self.website_url,
            }
        )
        return True
