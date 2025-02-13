from flask import flash
from app import mongodb
from datetime import datetime
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
        return check_password_hash(account["Pin_Number"], pin_no) if account else False

    def close_account(self, acc_no, emailID, pin_no):
        account = mongodb.Accounts.find_one({"Account_Number": str(acc_no)})
        if account and self.validate_pin(acc_no, pin_no):
            if emailID == account["EmailID"]:
                if not account["Close_date"]:
                    mongodb.Accounts.update_one(
                        {"Account_Number": str(acc_no)},
                        {
                            "$set": {
                                "Activity": False,
                                "Close_date": str(datetime.now().date()),
                            }
                        },
                    )
                    flash(
                        f"Your Account - {acc_no} has been closed Successfully. You can Re-Activate it anytime."
                    )
                else:
                    flash(f"Your Account - {acc_no} is already closed.")
            else:
                flash(
                    f"This Account - {acc_no} is not yours, So not possible to close it."
                )
        else:
            flash(
                f"This Account - {acc_no} is not found in the Database or Wrong Pin_number, So not possible to close it."
            )

    def delete_account(self, acc_no, pin_no):
        if self.validate_pin(acc_no, pin_no):
            result = mongodb.Accounts.delete_one({"Account_Number": str(acc_no)})
            if result > 0:
                mongodb.SavingsAccounts.delete_one({"Account_Number": str(acc_no)})
                mongodb.CurrentAccounts.delete_one({"Account_Number": str(acc_no)})
                flash(
                    f"Your Account - {acc_no} has been Deleted Successfully. You can collect your account balance from the cashier."
                )
            else:
                flash(
                    f"This Account - {acc_no} is not found in the Database or Wrong Pin_number, So not possible to delete it."
                )
        else:
            flash(
                f"This Account - {acc_no} is not found in the Database or Wrong Pin_number, So not possible to delete it."
            )

    def view_all_my_accounts(self, emailID):
        accounts = list(mongodb.Accounts.find({"EmailID": emailID}))
        return accounts if accounts else False
