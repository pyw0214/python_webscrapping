def open_account():
    print("New account has made")


def deposit(balance, money):
    print("deposit has completed. balance is {0} Won".format(balance + money))
    return balance + money


def withdraw(balance, money):
    if balance >= money:
        print("withdraw has completed. Balance : {0} Won".format(
            balance - money))
        return balance - money
    else:
        print(
            "Withdraw does not have completed. Balance : {0} Won".format(balance))
        return balance


def withdraw_night(balance, money):
    commission = 100  # extrafee
    return commission, balance - money - commission


balance = 0
balance = deposit(balance, 1000)
#balance = withdraw(balance, 500)

commission, balance = withdraw_night(balance, 500)
print("commission fee is {0}, balance is {1}".format(commission, balance))
