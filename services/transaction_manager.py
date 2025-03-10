from flask import flash
from app import mongodb
from datetime import datetime
from services.account_manager import AccountManager
from exceptions.exceptions import BankExceptions


class TransactionManager:
    def isActive(self, account):
        if account["Activity"]:
            return True
        else:
            flash(BankExceptions.accountIsInactive(account["Account_Number"]))
            return False

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
        if account and self.isActive(account):
            if store:
                self.store_in_mongodb(
                    str(acc_no), "SELF", "deposit", amount, str(datetime.now())
                )
            amount += account["Balance"]
            mongodb.Accounts.update_one(
                {"Account_Number": str(acc_no)}, {"$set": {"Balance": amount}}
            )
            flash(f"Successfully Deposited. Current Balance - ₹{amount}.")
        else:
            flash(BankExceptions.accountNotInDB(acc_no) + "So not possible to Deposit.")

    def withdraw_amount(self, acc_no, pin_no, amount):
        account = mongodb.Accounts.find_one({"Account_Number": str(acc_no)})
        if (
            account
            and AccountManager().validate_pin(acc_no, pin_no)
            and self.isActive(account)
        ):
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
                    BankExceptions.insufficientBalance(acc_no)
                    + "Cannot proceed with the withdrawal."
                )
        else:
            flash(
                BankExceptions.accountNotInDB(acc_no)
                + BankExceptions.wrongPin()
                + "So not possible to Withdraw."
            )

    def transfer_amount(self, acc_no, to_acc_no, pin_no, amount):
        account = mongodb.Accounts.find_one({"Account_Number": str(acc_no)})
        to_account = mongodb.Accounts.find_one({"Account_Number": str(to_acc_no)})
        if (
            account
            and AccountManager().validate_pin(acc_no, pin_no)
            and self.isActive(account)
        ):
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
                        BankExceptions.insufficientBalance(acc_no)
                        + "Cannot proceed with the transfer."
                    )
            else:
                flash(
                    BankExceptions.accountNotInDB(to_acc_no)
                    + "So not possible to transfer funds to it."
                )
        else:
            flash(
                BankExceptions.accountNotInDB(acc_no)
                + BankExceptions.wrongPin()
                + "So not possible to transfer funds from it."
            )

    def view_all_my_transactions(self, acc_no, pin_no):
        if AccountManager().validate_pin(acc_no, pin_no):
            transactions = list(
                mongodb.TransactionsHistory.find(
                    {
                        "$or": [
                            {"Account_Number": str(acc_no)},
                            {"Recipient_Account_Number": str(acc_no)},
                        ]
                    }
                )
            )
            return transactions if transactions else False
        else:
            flash(
                BankExceptions.accountNotInDB(acc_no)
                + BankExceptions.wrongPin()
                + "So not possible to view the transactions."
            )
            return False
