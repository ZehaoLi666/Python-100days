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
    rest=[]                                    # or is_prime = True                     
    for i in range(1 , number):
        if number % i == 0 : 
            rest.append(i)                     # is_prime = False
    if len(rest) > 2 : 
        print("It's not a prime number.")     
    else : 
        print("It's a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)
```

## Practice3 

if char is str:                                      判断 char是否为字符串， or if char in alphabet

position = alphabet.index(char)                      查看一个元素在列表中的索引位置

```
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(start_text, shift_amount, cipher_direction):
  end_text = ""
  if cipher_direction == "decode":
    shift_amount = shift_amount % 26
    shift_amount *= -1
  for char in start_text:
    if char is str:                                     # 判断 char是否为字符串， or if char in alphabet
      
      position = alphabet.index(char)                   # 查看一个元素在列表中的索引位置
      new_position = position + shift_amount
      end_text += alphabet[new_position]
    else:
      end_text += char
    
  print(f"Here's the {cipher_direction}d result: {end_text}")


from art import logo
print(logo)


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

game_status= False 
while game_status == False:                           # 自己加一个条件判断，完成while loop
  caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  status = input("Do you want to restart the game? (yes or no)")
  if status == "yes":
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
  if status == "no":
    game_status= True
```

 
