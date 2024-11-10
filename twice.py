# A programme that uses the function do_twice to print a message to the screen twice

def do_twice(f):
    f()
    f()

def print_spam():
    print ("spam")

do_twice(print_spam)










