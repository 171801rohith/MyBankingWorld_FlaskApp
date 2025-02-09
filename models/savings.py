from account import Account


class Savings(Account):
    def __init__(self, name, balance, pin_number, privilege, date_of_birth, gender):
        super().__init__(name, balance, pin_number, privilege)
        self.gender = gender
        self.date_of_birth = date_of_birth
