import math
import re
# import sin, cos, sqrt, log
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

def getPostfixExpT(inExp):
    """处理中缀表达式来得到后缀表达式"""
    priority = {'*':2,'/':2,'+':1,'-':1,'(':0}
    stack, res, temp = [],[],[]
    for c in inExp + ' ': # 为了访问到最后的字符,需要加上空格
        if c.isdigit() or c=='.': # 处理遇到数字的情况
            temp.append(c)
            continue
        if temp:
            res.append(''.join(temp))
            temp.clear()
        if c in priority.keys() and c!='(': # 处理遇到运算符号的情况
            if not stack:
                stack.append(c)
            else:
                while stack and priority[stack[-1]]>=priority[c]:
                    res.append(stack.pop())
                stack.append(c)
        elif c=='(':
            stack.append(c)
        elif c==')':
            t = stack.pop()
            while stack and t!='(':
                res.append(t)
                t = stack.pop()
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
        # print(stack)
        if n.isdigit() or '.'in n:
            stack.append(float(n))
            if len(postExp)==1:
                return n
        elif n in opt.keys():
            num = stack.pop()
            res = opt[n](stack,num)
            stack.append(res)
    
    return res

def factorial(exp1,exp2=None): # 阶乘函数
    if '.' in exp1 or '-' in exp1 or exp2:
        raise ValueError('illegal expression')
    if exp1=='0' or exp1=='1':
        return '1'
    if int(exp1) > 101: #超过101!就会显示不完整
        raise ValueError('number is too big')
    res = 1
    for i in range(1,int(exp1)+1):
        res *= i
    return ' '+str(res)+' '

def replace(exp): #将表达式替换为eval认识的
    dic = {'ln':'log', 'E':E, 'Pi':PI,}
    #print('gp0:',exp.group(0))
    if exp.group(0) in dic.keys():
        return dic[exp.group(0)]
    elif '^' in exp.group(0):
        return '**'
    elif '!' in exp.group(0):
        t = exp.group(0).split('!')
        return factorial(*exp.group(0).split('!'))

def myEvalTemp(expr):
    exceptList=['cos','sin','log','sqrt','**'] # 目前无法处理
    if not expr:
        raise ValueError('illegal expression')
    for eLst in exceptList:
        if eLst in expr:
            res = eval(expr)
            return res
    try:
        exp=re.sub(r'ln|E|Pi|\-?\d+(.\d+)?\!|\^',replace,expr)
        print('exp==',exp)
        res = calculate(getPostfixExp(exp))
    except BaseException:
        raise SyntaxError('illegal expression')
    return res
    
# 以下为测试用代码
if __name__=='__main__': 
    """test only"""
    # pst=getPostfixExp('10+10*(3-2)+1*3+4')
    # print('pst'+str(pst))
    # res=calculate(pst)
    # print(res)
    # print(myEvalTemp('1+2 * 3 / 4 +100'))
    # pstt = '1.1+1.2*3+(4-6)'
    # print(myEvalTemp(pstt))
    print(getPostfixExpT('1+3.4*(5-6)/8'))