# -*- coding:utf-8 -*-

def scaleAndCurve(score):
    if 90 <= score <= 100:
        return "A"
    elif 80 <= score <= 89:
        return "B"
    elif 70 <= score <= 79:
        return "C"
    elif 60 <= score <= 69:
        return "D"
    elif score < 60:
        return "F"


if __name__ == '__main__':
    score = int(input("Score: "))
    print("Scale: ", scaleAndCurve(score))
