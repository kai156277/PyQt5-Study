# -*- coding:utf-8 -*-

def salesTax(monetary):
    return monetary * 0.03

if __name__ == '__main__':
    monetary = int(input("Monetary: "))
    print("Sale Tax: ", salesTax(monetary))
