from flask_pymongo import PyMongo
from app import mongodb


class AccountRepository:
    @classmethod
    def generate_account_number(cls):
        cls.new_account_number = mongodb.Counter.find_one_and_update(
            {"_id": "account_no"},
            {"$inc": {"latestAccGen": 1}},
            upsert=True,
            return_document=PyMongo.ReturnDocument.AFTER,
        )
        return str(cls.new_account_number["latestAccGen"])

    @classmethod
    def get_account(cls, account_number):
        cls.account = mongodb.Accounts.find_one({"Account_number": account_number})
        if cls.account:
            return cls.account
        else:
            return None
