import time
# def add(n1, n2):
#   return n1 + n2

# def subtract(n1, n2):
#   return n1 - n2

# First class objects - you can pass a function around like an argument

# def calculate(calc_function, n1, n2):
#   return calc_function(n1, n2)

# result = calculate(subtract, 1, 5)
# print(result)

# Nested functions

# def outer_function():
#   print("I'm outer")

#   def nested_function():
#     print("I'm inner")

#   nested_function()

# outer_function()

# Functions can be returned from other functions

# def outer_function():
#   print("I'm outer")

#   def nested_function():
#     print("I'm inner")

#   return nested_function

# inner_function = outer_function()
# inner_function()

# DECORATORS

def delay_decorator_function(function):
  def wrapper_function():
    time.sleep(2)
    function()

  return wrapper_function

@delay_decorator_function
def say_hello():
  print("Hello")

def say_bye():
  print("Bye")

@delay_decorator_function
def say_greeting():
  print("How are you?")

say_hello()
say_bye()
say_greeting()
