#!/usr/bin/evn python
# -*- coding: utf-8 -*-

import sys


def calculate_steps_collection_number(n):
    """
    题目:
    河边 N 块石头排成一排，一只青蛙蹲在第 1 块石头上，打算跳到第 N 块石头上。 
    青蛙每次可以向前跳过一块石头或者两块石头，即从第 K 块石头可以跳到第 K+1 或者 K+2 块石头。
    问青蛙从第 1 块石头跳到第 N 块石头，共有多少种不同的方式? 请编程实现，已知 1 <= N <= 40。 

    思路:
    反向思考，从第N块石头跳到第1块石头。由于青蛙只能跳1或者2块石头，模型可以抽象为：
    从第N块石头起跳的跳数 = 从第N-1块石头起跳的跳数 + 从第N-2块石头起跳的跳数
    但N in (1, 2, 3)时，不适用上面的公式

    >>> print calculate_steps_collection_number(6)
    8
    """

    n -= 1
    steps = [0, 1, 2]
    for i in xrange(3, n + 1):
        steps.append(steps[i-1] + steps[i-2])

    return steps[n]






if __name__ == "__main__":
    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print "Usage: python %s [5]" % sys.argv[0]
        sys.exit(1)

    n = int(sys.argv[1])
    print calculate_steps_collection_number(n)
    
