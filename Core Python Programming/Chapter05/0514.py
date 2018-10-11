# -*- coding:utf-8 -*-

def interest(account):
    return account * (1 + 0.0035) ** 365

if __name__ == "__main__":
    account = float(input("account: "))
    endAccount = interest(account)
    print("end account: ", endAccount)
    print("rate: ", endAccount / account)
