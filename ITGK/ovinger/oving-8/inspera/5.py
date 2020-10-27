def derivative(x,function):
    h = 1e-8
    return (f(x+h)-f(x))/h

def f(x):
    return x**2 + 2*x + 13
print(round(derivative(3,f),2))