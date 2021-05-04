def say_hello(who): # 'who' is argument
    print("hello", who)
    print("bye")

say_hello("dev") # execution
say_hello # non-executable

def plus(a, b):
    print(a + b)

def minus(a, b=0): # 'b=0' means the default value is 0
    print(a + b)

plus(2 ,5)
minus(2)
