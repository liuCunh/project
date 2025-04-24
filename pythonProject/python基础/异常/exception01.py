# 语法错误和异常
# 语法错误

# 异常：程序运行的时候报出来的。 xxxError
# def chu(a, b):
#     return a / b
#
#
# chu(1, 0)  # ZeroDivisionError: division by zero
# print('----------->')

# 异常处理
"""
格式：
try:
    可能出现异常的代码
except:
    如果有异常执行的代码
[finally:
    无论是否存在异常，都会被执行的代码]


情况一：
    try:
        有可能产生多种异常
    except 异常类型1:  异常的类型
        print(...)
    except 异常类型2:
        pass
    except Exception:
        pass

except情况种类比较多时，异常类型要注意，Exception要放到最后的位置

情况二：获取Exception的错误原因
    try:
        有可能产生多种异常
    except 异常类型1:  异常的类型
        print(...)
    except 异常类型2:
        pass
    except Exception as err:
        print(err)  ---> err是程序错误的原因

    eg:  pop from empty list  --> 从空的列表中删除内容

"""


def func():
    try:
        n1 = int(input('num1='))
        n2 = int(input('num2='))

        per = input('输入运算符号(+ - * /)：')
        res = 0
        if per == '+':
            res = n1 + n2
        elif per == '-':
            res = n1 - n2
        elif per == '*':
            res = n1 * n2
        elif per == '/':
            res = n1 / n2
        else:
            print('符号错误')
        print(f'res={res}')

        # 操作列表，错误模拟
        list1 = []
        list1.pop()

        # 文件操作
        with open(r'd:\pythonDir\test\aa.txt', 'r') as wrestream:
            print(wrestream.read())

    except ZeroDivisionError:
        print('除数为零！')
    except ValueError:
        print('输入不是数字！')
    # except FileNotFoundError:
    #     print('路径有问题')
    # except NameError:
    #     pass
    except Exception as err:
        print('出错了！', err)


func()
print('---->')