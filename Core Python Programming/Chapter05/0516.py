# -*- coding:utf-8 -*-

def payment(balance, paid):
    if balance < paid:
        return balance, 0
    else:
        return paid, balance - paid

if __name__ == '__main__':
    balance = float(input("Enter opening balance: "))
    paid = float(input("Enter monthly payment: "))

    print("      Amount  Remaining")
    print("Pymt#  Paid    Balance")
    print("-----  ----    -------")

    print("{:3d}  {:7.2f}  {:7.2f}".format(0, 0, balance))
    month = 1
    while(True):
        paid, balance = payment(balance, paid)
        print("{:3d}  {:7.2f}  {:7.2f}".format(month, paid, balance))
        month += 1
        if balance == 0:
            break
