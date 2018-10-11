# -*- coding:utf-8 -*-

import random as rd
import sys

if __name__ == "__main__":
    num = rd.randint(0, 100)
    rdList = list()
    for i in range(num):
        rdList.append(rd.randint(0, 1000))

    sortList = list()
    for i in range(num):
        index = rd.randint(0, num)
        sortList.append(rdList[index])

    print("Sort List Num: ", len(sortList))
    print("No Sort List: ")
    print(sortList)
    sortList.sort()
    print("Sort List: ")
    print(sortList)
