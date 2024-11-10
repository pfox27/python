# A programme that uses the function do_twice to print a message to the screen twice

def do_twice(func, b):
    func(b)
    func(b)

def do_four(f, s):
    do_twice(f,s)
    do_twice(f,s)

def print_string(x):
    print (x)

do_four(print_string, "spam")


