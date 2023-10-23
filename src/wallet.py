class InsufficientAmount(Exception):
    pass


class Wallet(object):

    def __init__(self, initial_amount=0):
        self.balance = initial_amount

    def spend_cash(self, amount):
        if self.balance < amount:
            raise InsufficientAmount('Not enough available to spend {}'.format(amount))
        self.balance -= amount

    def add_cash(self, amount):
        self.balance += amount
aws_secret = "dsafadsfds"
my_secret_password = "adfs.kgjhdflkghadfskl;gjerqkjlgh45ejkgnadrf"
real_password = "ThisIsMYRealPassword##%R#@%"
#test
med_stripeKey = "rk_live_9sOOJGPdSoBA6V2GJJCDTANR"
