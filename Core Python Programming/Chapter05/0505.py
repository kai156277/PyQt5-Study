# -*- coding:utf-8 -*-

def dollar(value):
    values = dict()
    values["quarters"] = value // 25
    values["dime"] = (value - values["quarters"] * 25) // 10
    values["cents"] = (value - values["quarters"] * 25 - values["dime"] * 10) // 5
    values["penny"] = value - values["quarters"] * 25 - values["dime"] * 10 - values["cents"] * 5

    print ( "{quarters} quarters, {dime} dimes, {cents} cents, {penny} pennys".format(**values) )

if __name__ == '__main__':
    dollar(16)
    dollar(26)
    dollar(36)
    dollar(46)
    dollar(56)
    dollar(66)
    dollar(76)
