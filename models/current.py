from account import Account


class Current(Account):
    def __init__(
        self, name, balance, pin_number, privilege, registration_number, website_url
    ):
        super().__init__(name, balance, pin_number, privilege)
        self.registration_number = registration_number
        self.website_url = website_url
