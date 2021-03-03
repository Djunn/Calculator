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
# 数字越大优先级越高
priority = {'*':2,'/':2,'+':1,'-':1,'(':0}

def getPostfixExp(inExp):
    stack = []
    res = []
    temp = []
    for c in inExp+' ': #不加空格有可能访问不了最后的字符
        print('s'+str(stack))
        print('res:'+str(res))
        if temp: #处理连续的数字
            res.append(''.join(temp))
            temp.clear()
        if c.isdigit():
            temp.append(c)
            continue
        elif c in priority.keys() and c!='(' and c!=')':
            if not stack:
                stack.append(c)
            else:
                while stack:
                    if priority[stack[-1]] >= priority[c]:
                        res.append(stack.pop())
                    else:
                        break
                stack.append(c)
        elif c=='(':
            stack.append(c)
        elif c==')':
            while stack:
                t = stack.pop()
                if(t=='('):
                    break
                else:
                    res.append(t)

    while stack:
        res.append(stack.pop())
    return res

def myEval(expr):
    pass
    

#以下为调试用代码
if __name__=='__main__': 
    print(getPostfixExp('1+(2-3)*4+4/2')) 