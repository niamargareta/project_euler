def abc(foo):
    print('the abc function was given:', foo)
    return foo+3


def bar(foo):
    print('the bar function was given:', foo)
    abc(foo)
    return foo-2


def car(foo):
    print('the car function was given:', foo)
    return foo*2

x = abc(3)
print('it returned :', x)
x = car(5)
print('it returned :', x)
x = abc(4)
print('it returned :', x)

