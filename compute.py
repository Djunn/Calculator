import math
# from math import sin, cos, sqrt, log
PI = 3.141592653589793
E = 2.718281828459045

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
def getPostfixExp(inExp):
    # 数字越大优先级越高
    priority = {'*':2,'/':2,'+':1,'-':1,'(':0}
    stack,res,temp=[],[],[]
    for c in inExp+' ': # 不加空格有可能访问不了最后的字符
        if c.isdigit():
            temp.append(c)
            continue
        if temp: # 处理连续的数字
            res.append(''.join(temp))
            temp.clear()
        if c in priority.keys() and c!='(' and c!=')':
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

# 计算后缀表达式
def calculate(postExp):
    opt = {
        '-': lambda x,n: x.pop() - n,
        '+': lambda x,n: x.pop() + n,
        '*': lambda x,n: x.pop() * n,
        '/': lambda x,n: x.pop() / n,
    }
    stack = []
    for n in postExp:
        print(stack)
        if n.isdigit():
            stack.append(int(n))
        elif n in opt.keys():
            num = stack.pop()
            res = opt[n](stack,num)
            stack.append(res)
    
    return res


def myEval(expr):
    if not expr:
        raise ValueError('illegal expression')
    res = calculate(getPostfixExp(expr))
    return res
    
# 以下为测试用代码
if __name__=='__main__': 
    pst=getPostfixExp('10+10*(3-2)+1*3+4')
    print('pst'+str(pst))
    res=calculate(pst)
    print(res)