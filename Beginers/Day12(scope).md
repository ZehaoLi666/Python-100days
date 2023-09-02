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

If you want to use the global variable in the add() function, use `global` to import global variable in the function.
### Don't try to modify the global variable in a local function.
So what if you want to use global variable in the local function? use `return`
```
variable =1

def add():
  
  return variable + 1
  print(variable)
```

