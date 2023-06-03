# LEGB

# local --> in function
# enclosing --> одна функция в нутри другой функции
# global --> a = 2
# built-in --> зарезервированное значение

"""# var_1 = 5
def func_1():
    global var_1
    var_1 = 10
    print(f'var_1 in function - {var_1}')

func_1()
print(f'var_1 out function - {var_1}')

var1 = 5
def func_2():
    global var1
    print(var1)
    var1 = 2

func_2()
print(var1)

var_1 = 5
def func_3():
    var_1 = 10
    def func_4():
        print(var_1)

    func_4()
func_3()
print(var_1)"""

"""a = 6
b = 15
def first():
    a = 10
    def second():
        nonlocal a
        a = 1
        global b
        b = 3
    second()
    print('a - ', a)
first()
print('b - ', b)
print('a - ', a)

print(f'local - {locals()}')
print(f'global - {globals()}')"""


# args -
# kwargs -

# def black_hole(*args):
#     print(type(args))
#     for argument in args:
#         print(argument, end = ' ')
#
# args = 3, 5, 18,' name', 'address', 4*5
# black_hole(args)
# print()
# black_hole(3, 5, 18,' name', 'address', 4*5)
# print()
#
# def black_hole_named(**kwargs):
#     print(type(kwargs))
#     for argument in kwargs:
#         print(argument)
#     for key, value in kwargs.items():
#         print(key,  value, sep=':')
# black_hole_named(name='Nick', auto='BMW', age=15, school=217)


def black_hole_full(*args, **kwargs):
    for arg in args:
        print(arg, end=' ')
    print()
    for key, value in kwargs.items():
        print(key, value, sep=':',  end=' ')
    print()
black_hole_full(3, 5, 18,' name', 'address', 4*5, name='Nick', auto='BMW', age=15, school=217)


# def bh_mix(a=5, b=1.6, *args, **kwargs):



def way(v,t):
    s = v * t
    print(s)
lst = [80,3]
way(*lst)

dict1 = {'v': 80, 't': 3}
way(**dict1)

dict2 = {'c':5, 'd':12}
lst1 = [2]
def some(a,b,c,d):
    print(a,b,c,d)

some(1,*lst1,**dict2)
