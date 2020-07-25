class User:
    def __init__(self, name):
        self.money = 0
        self.name = name
        # self.type = amount
    # starting money
    def make_deposit(self, amount):
        self.money += amount
        return self
    def make_withdrawal(self, amount):
        # if self.money < amount
        self.money -= amount
        # self.money = self.money - amount
        print("withdrawing:", amount)
        return self

    def display_user_balance(self):
        print(f"{self.name} Balance: ${self.money}")
        return self

    def transfer_money(self, other_user, amount):
        self.money -= amount
        print("transfering:", amount)
        other_user.money += amount
        return self


glaceon = User('glacia')
umbreon = User('umbra')
glaceon.make_deposit(1000000).display_user_balance().make_withdrawal(69).display_user_balance()
umbreon.display_user_balance()
glaceon.transfer_money(umbreon, 1)
umbreon.display_user_balance()
glaceon.display_user_balance()



# glaceon = User('glacia')
# umbreon = User('umbra')
# glaceon.make_deposit(1000000)
# glaceon.display_user_balance()
# glaceon.make_withdrawal(69)
# glaceon.display_user_balance()
# umbreon.display_user_balance()
# glaceon.transfer_money(umbreon, 1)
# umbreon.display_user_balance()
# glaceon.display_user_balance()