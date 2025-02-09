from datetime import datetime


class Account:
    def __init__(self, name, balance, pin_number, privilege):
        self.name = name
        self.pin_number = pin_number
        self.balance = balance
        self.privilege = privilege
        self.is_active = True
        self.open_date = datetime.now()
        self.close_date = None
