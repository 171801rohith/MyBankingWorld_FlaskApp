from flask import flash
from app import mongodb
from werkzeug.security import check_password_hash


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
            flash(
                f"This Account - {acc_no} is not found in the Database, So not possible to view is_active."
            )
            return None

    def validate_pin(self, acc_no, pin_no):
        account = mongodb.Accounts.find_one({"Account_Number": str(acc_no)})
        if account:
            return check_password_hash(account["Pin_Number"], pin_no)
        else :
            return False