#!/bin/python3

import math
import os
import random
import re
import sys

""" problem: https://www.hackerrank.com/challenges/30-arrays """

__author__ = "Shovra Das"


if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    for i in range(n):
        print(arr[n-i-1], end=' ')
