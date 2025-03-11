class BankExceptions:
    @classmethod
    def dailyLimitReached(cls):
        return "Sorry you cannot proceed with the Transaction as you have reached the daily limit. "

    @classmethod
    def ageLimit(cls):
        return (
            "Your age is less than 18, You cannot open an account without a Nominee. "
        )

    @classmethod
    def pinLength(cls):
        return "Enter a valid 4 to 6 digits pin. "

    @classmethod
    def onlyLetters(cls):
        return "Name should only consist letters. "

    @classmethod
    def insufficientInitialBalance(cls):
        return "Initial Balance should be greater than ₹1000. "

    @classmethod
    def insufficientBalance(cls, acc_no):
        return f"Your Account - {acc_no} does not have enough funds. "

    @classmethod
    def emailNotInDB(cls, email):
        return (
            f"Your EmailID - {email} not found in Database or Recheck your Password. "
        )

    @classmethod
    def emailAlreadyExists(cls):
        return "EmailID Already Exists. Try to Login with your Password. "

    @classmethod
    def accountIsInactive(cls, acc_no):
        return f"This account - {acc_no} is Inactive, So you cannot do any sought of Transactions. "

    @classmethod
    def accountNotInDB(cls, acc_no):
        return f"This Account - {acc_no} is not found in the Database. "

    @classmethod
    def wrongPin(cls):
        return "Incorrect Pin Number. "
