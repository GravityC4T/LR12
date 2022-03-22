#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def recursion(n):
    if n == 1:
        return 1
    return n + recursion(n - 1)


if __name__ == '__main__':
    n = int(input("Enter n: "))
    summary = 0
    for i in range(1, n + 1):
        summary += i
    print("Iterative sum: " +str(summary) )
    print("Recursion sum: " +str(recursion(n)) )