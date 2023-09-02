```
variable =1

def add():
  variable = 2
  print(variable)

print(variable)
```
In this case, the first variable will output 2, the second variable will output 1. Because the first variable is global variable. The second variable in the add() function is local variable.

```
variable =1

def add():
  global variable
  variable += 2
  print(variable)
```

if you want to use the global variable in the add() function, use `global` to import global variable in the function.
