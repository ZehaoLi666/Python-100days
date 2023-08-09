# return 

### output
output of a function, same as print()

### stop 
only use ``` return ``` with values can stop a function

### serve as a input for next function 
This is the differnece between print and return
```
def function1():
  XXXXXX
  return A

function2(A):
  XXXXXX
  
```

# Docstrings

to add some explantion of the function you write

 use "```" to explain  

# Practice

### recursion 
reuse the function at the end of the same function, to repeat running the function
 
```
from replit import clear
from art import logo

def add(n1, n2):
  return n1 + n2

def subtract(n1, n2):
  return n1 - n2

def multiply(n1, n2):
  return n1 * n2

def divide(n1, n2):
  return n1 / n2

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}

def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()       # repeat calling calculator()         

calculator()

```
