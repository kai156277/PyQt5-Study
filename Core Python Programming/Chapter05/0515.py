# -*- coding:utf-8 -*-

def getGCD(first, second):
    if first == 0 or second == 0:
        return 0
    if first < second:
        second, first = first, second
    
    #  print("first: %d" % first)
    #  print("second: %d" % second)
    tmp = first % second
    if tmp == 0:
        return second
    else:
        return getGCD(second, tmp)

def getLCM(first, second):
    if first == 0 or second == 0:
        return 0
    return int(first * second / getGCD(first, second))

if __name__ == '__main__':
    print("first, second: GCD, LCM")
    print("10, 20: ", getGCD(10, 20), getLCM(10, 20))
    print("11, 20: ", getGCD(11, 20), getLCM(11, 20))
    print("10, 22: ", getGCD(10, 22), getLCM(10, 22))
    print("70, 20: ", getGCD(70, 20), getLCM(70, 20))
    print("60, 20: ", getGCD(60, 20), getLCM(60, 20))
    print("50, 25: ", getGCD(50, 25), getLCM(50, 25))
    print("20, 20: ", getGCD(20, 20), getLCM(20, 20))
    print("10,  0: ", getGCD(10,  0), getLCM(10,  0))
    print("17, 23: ", getGCD(17, 23), getLCM(17, 23))
    print("11, 27: ", getGCD(11, 27), getLCM(11, 27))
