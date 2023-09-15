# -----------------Passing & Nesting Functions-----------------


# functions are first-clss objects, which can be passed around as arguments e.g. int/string/float etc.
def add(n1, n2):
    return n1 + n2

def multiply(n1, n2):
    return n1 * n2


def calculate(calc_function, ni, n2):
    return calc_function(n1, n2)


# -----------------Nested functions-----------------

def outer_function():
    print("I'm outer")

    def nested_function():
        print("I'm inner")

    return nested_function


# functions cna be returned from other functions

inner_function = outer_function()
inner_function()



# -----------------decorator function-----------------

def decorator_func(function):
    def wrapper_func():
        function()
    
    return wrapper_func


# example 

import time 

def delay_decor(function):
    # do sth before the function
    time.sleep(2)

    # modify the function
    def wrapper_func():
        function()
    
    # do sth after the function

    return wrapper_func


@delay_decor
def say_hello():

    print("Hello")


@delay_decor
def say_bye():
    print("Bye")


@delay_decor
def say_greeting():
    print("How are you?")

