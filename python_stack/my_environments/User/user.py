class User:
    def __init__(self, name):
        self.money = 0
        self.name = name
        # self.type = amount
    # starting money
    def make_deposit(self, amount):
        self.money += amount
    def make_withdrawal(self, amount):
        # if self.money < amount
        self.money -= amount
        # self.money = self.money - amount
        print("withdrawing:", amount)

    def display_user_balance(self):
        print(f"{self.name} Balance: ${self.money}")
    def transfer_money(self, other_user, amount):
        self.money -= amount
        print("transfering:", amount)
        other_user.money += amount




glaceon = User('glacia')
umbreon = User('umbra')
glaceon.make_deposit(1000000)
glaceon.display_user_balance()
glaceon.make_withdrawal(69)
glaceon.display_user_balance()
umbreon.display_user_balance()
glaceon.transfer_money(umbreon, 1)
umbreon.display_user_balance()
glaceon.display_user_balance()