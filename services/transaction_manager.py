from flask import flash
from app import mongodb
from datetime import datetime
from services.account_manager import AccountManager


class TransactionManager:
    def store_in_mongodb(self, acc_no, to_acc_no, type, amount, time):
        mongodb.TransactionsHistory.insert_one(
            {
                "Account_Number": acc_no,
                "Recipient_Account_Number": to_acc_no,
                "Transaction_Type": type,
                "Transaction_Amount": amount,
                "Date_Time": time,
            }
        )

    def deposit_amount(self, acc_no, amount, store=True):
        account = mongodb.Accounts.find_one({"Account_Number": str(acc_no)})
        if account:
            if store:
                self.store_in_mongodb(
                    str(acc_no), "SELF", "deposit", amount, str(datetime.now())
                )
            amount += account["Balance"]
            mongodb.Accounts.update_one(
                {"Account_Number": str(acc_no)}, {"$set": {"Balance": amount}}
            )
            return True
        else:
            flash(
                f"This Account - {acc_no} is not found in the Database, So not possible to Deposit."
            )

    def withdraw_amount(self, acc_no, pin_no, amount):
        account = mongodb.Accounts.find_one({"Account_Number": str(acc_no)})
        if account and AccountManager().validate_pin(acc_no, pin_no):
            self.store_in_mongodb(
                str(acc_no), "BANK", "withdraw", amount, str(datetime.now())
            )
            if amount <= account["Balance"]:
                amount = account["Balance"] - amount
                mongodb.Accounts.update_one(
                    {"Account_Number": str(acc_no)}, {"$set": {"Balance": amount}}
                )
                flash(f"Successful Withdrawal. Current Balance - ₹{amount}.")
            else:
                flash(
                    f"Your Account - {acc_no} does not have enough funds. Cannot proceed with the withdrawal."
                )
        else:
            flash(
                f"This Account - {acc_no} is not found in the Database or Wrong Pin_number, So not possible to Withdraw."
            )

    def transfer_amount(self, acc_no, to_acc_no, pin_no, amount):
        account = mongodb.Accounts.find_one({"Account_Number": str(acc_no)})
        to_account = mongodb.Accounts.find_one({"Account_Number": str(to_acc_no)})
        if account and AccountManager().validate_pin(acc_no, pin_no):
            if to_account:
                deposit = amount
                self.store_in_mongodb(
                    str(acc_no), str(to_acc_no), "transfer", amount, str(datetime.now())
                )
                if amount <= account["Balance"]:
                    amount = account["Balance"] - amount
                    mongodb.Accounts.update_one(
                        {"Account_Number": str(acc_no)}, {"$set": {"Balance": amount}}
                    )
                    self.deposit_amount(to_acc_no, deposit, False)
                    flash(f"Successful Transfer. Current Balance - ₹{amount}.")
                else:
                    flash(
                        f"Your Account - {acc_no} does not have enough funds. Cannot proceed with the transfer."
                    )
            else:
                flash(
                    f"This Account - {to_acc_no} is not found in the Database , So not possible to transfer funds to it."
                )
        else:
            flash(
                f"This Account - {acc_no} is not found in the Database or Wrong Pin_number, So not possible to transfer funds from it."
            )
