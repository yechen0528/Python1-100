def calc(*args, init_value, op, **kwargs):
    result = init_value
    for arg in args:
        if type(arg) in (int, float):
            # 通过对高阶函数的运用，calc函数不再和加法运算耦合，所以灵活性和通用性会变强
            result = op(result, arg)
    for value in kwargs.values():
        if type(value) in (int, float):
            result = op(result, value)
    return result


def add(x, y):
    return x + y


def mul(x, y):
    return x * y


a = calc(1, 2, 3, init_value=0, op=add, x=4, y=5)  # op=add,调用函数需要在函数名后面跟上圆括号，而把函数作为参数时只需要函数名即可
print(a)