# coding:utf-8
"""
汉诺塔：
    1.将n-1层铁饼，从A经过C移动到B
    2.然后将A铁饼移动到C
    3.最后将铁饼，从B经过A移动到C
"""

def honio(n,A,B,C):
    if n>0:
        honio(n-1,A,C,B)
        print(f"{A}移动到{C}")
        honio(n-1,B,A,C)

honio(3,"A","B","C")