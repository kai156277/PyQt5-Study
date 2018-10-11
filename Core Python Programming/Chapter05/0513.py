# -*- coding=utf-8 -*-

def conversion(hours, minutes):
    return hours * 60 + minutes

if __name__ == "__main__":
    hours = int(input("hours: "))
    minutes = int(input("minutes: "))

    print("total minutes: ", conversion(hours, minutes))
