# https://www.hackerrank.com/challenges/py-set-add/problem

__author__ = "Shovra Das"

n = int(input().strip())

distinct_countries = set()
for _ in range(n):
    distinct_countries.add(input().strip())

print(len(distinct_countries))
