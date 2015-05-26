def square(s):
    return s*s

def cube(s):
    return s**3

def sum_of(f,x,y):
    return f(x) + f(y)

print sum_of(square,3,4)
print sum_of(cube,3,4)


