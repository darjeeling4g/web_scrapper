def plus(a, b):
    return a - b

result = plus(b=30, a=1) #keyworded argument
print(result)

def say_hello(name, age):
    return f"hello {name} you are {age} years old" # or "hello" + name + "you are" + age + "years old"

hello = say_hello("dev", "12")
print(hello)
