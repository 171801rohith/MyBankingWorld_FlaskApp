from flask import flash
from app import mongodb


class AccountManager:
    def isActive(self, acc_no, emailID):
        account = mongodb.Accounts.find_one({"Account_Number": str(acc_no)})
        if account:
            if emailID == account["EmailID"]:
                return account["Activity"]
            else:
                flash(
                    f"This Account - {acc_no} is not yours, So not possible to view is_active."
                )
            return None
        else:
            return None
