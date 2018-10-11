# -*- coding:utf-8 -*-


if __name__ == '__main__':
    arithmetic = input("Arithmetic: ").strip()
    tmps = arithmetic.split(" ")
    if tmps[1] == "+":
        print("value: ", float(tmps[0]) + float(tmps[2]))
    elif tmps[1] == "-":
        print("value: ", float(tmps[0]) - float(tmps[2]))
    elif tmps[1] == "*":
        print("value: ", float(tmps[0]) * float(tmps[2]))
    elif tmps[1] == "/":
        print("value: ", float(tmps[0]) / float(tmps[2]))
    elif tmps[1] == "%":
        print("value: ", float(tmps[0]) % float(tmps[2]))
    elif tmps[1] == "**":
        print("value: ", float(tmps[0]) ** float(tmps[2]))

