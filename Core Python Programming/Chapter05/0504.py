# -*- coding:utf-8 -*-

def isLeapYear(year):
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        return True
    else:
        return False

if __name__ == '__main__':
    print( "1992 is leap Year :", isLeapYear(1992) )
    print( "1996 is leap Year :", isLeapYear(1996) )
    print( "2000 is leap Year :", isLeapYear(2000) )
    print( "1900 is leap Year :", isLeapYear(1900) )
    print( "1967 is leap Year :", isLeapYear(1967) )
    print( "2400 is leap Year :", isLeapYear(2400) )
