# Paraments and Arguments 
Arguments are the true data you are going to use in the function.
Paraments are the name of the data. 

# Two ways to input variables
### 1. Positional Argument
```
def my_function(a,b,c)
         do function1 with a
         do function2 with b
         do function3 with c

my_function(1,2,3) # The variables you input will be executed in order 
```

### 2. Keyword Argument
```
def my_function2(name1,name2,names3)
     name1 = a, name2 = b, name3 = c,
     do function1 with name1
     do function2 with name2
     do function3 with name3

my_function2(name1=a,name2=b,names3=b)  # Associate specfic argument to specific parament
```

# Practice 
## Practice1 
```
import math 
a = 2.1455
b = math.ceil(a)  # b =3, 取a的上限
```
## Practice2

You need to write a function that checks whether if the number passed into it is a prime number or not.
e.g. 2 is a prime number because it's only divisible by 1 and 2.
But 4 is not a prime number because you can divide it by 1, 2 or 4.

```
def prime_checker(number):
    rest=[]
    for i in range(1 , number):
        if number % i == 0 : 
            rest.append(i) 
    if len(rest) > 2 : 
        print("It's not a prime number.")
    else : 
        print("It's a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)
```

 
