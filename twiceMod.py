# A programme that uses the function do_twice to print a message to the screen twice

def do_twice(f, s):
    f(s)
    f(s)

def print_string(x):
    print (x)

do_twice(print_string, "spam")










