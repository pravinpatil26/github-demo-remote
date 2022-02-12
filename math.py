# Add implimentation
def add(x, y);
    return x+y

# Sub implimentation
def subtract(x, y);
    return x-y              # on master branch

# Mul implimentation
def multiply(x, y);
    return x*y          # on bug456

# Div implimentation
def division(x, y);
    if y==0:                        # on bug789
        return divide_by_0_error
    else:
        return x/y
