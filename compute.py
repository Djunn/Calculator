import math
# from math import sin, cos, sqrt, log
"""
运算优先级(设定):

"""
PI = math.pi
E = math.e

def myCos(n):
    return math.cos(n)

def mySin(n):
    return math.sin(n)

def mySqrt(n):
    if n<0:
        raise ValueError(r'math domain error')
    return n**(1/2)

def myLog(n):
    return math.log(n) 


# 数学表达式运算函数 
# 数字越小优先级越高
priority = {'(':1,'*':2,'/':2,'+':3,'-':3}

def getPostfixExp(inExp):
    stack = []
    res = []
    temp = []
    for c in inExp:
        if c.isdigit():
            temp.append(c)
            continue
        if temp:
            res.append(''.join(temp))
            temp.clear()
        if c in priority.keys():
            if not stack or priority[stack[-1]] < priority[c]:
                stack.append(c)
                continue
            else:
                res.append(stack.pop())
        if c=='(':
            stack.append(c)
        elif c==')':
            t = stack.pop()
            while t!='(':
                res.append(stack.pop)
    while stack:
        res.append(stack.pop())
    return res

def myEval(expr):
    pass
    

#以下为调试用代码
if __name__=='__main__': 
    print(getPostfixExp(' 1 + 2 - 3 * 4 '))