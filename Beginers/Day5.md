# 1. for loop 
for in loop usually could be used in list data 
```
for item in range: 
  function
 ``` 
## exercise 1 (calculate average value from a list)
### way 1
```
student_heights = input("Input a list of student heights ").split()  # split() transfer string into a list 
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])  # transfer the item in the list from string into integer

total_height=0
for item in student_heights:
    total_height += item

number = 0 
for student in student_heights:
  number += 1

print(round(total_height/number))
```
### way2 len() count how many items in a list,   sum() calculate the total number in a list 
```
print(round(sum(student_heights) / len(student_heights)))
```
## exercise2: (select the highest score in a list)
### Way1：
```
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)

highest_score=0 
for score in student_scores: 

    if score > highest_score    :
        highest_score =score
    else: 
        pass
print(f"The highest score in the class is: {highest_score}")
```
### Way2： max() min() select the max and min value in a list
```
print(max(student_scores))
print(min(student_scores))
```
# 2. range()
# instead of looping in a list, we can decide a range to loop 
```
for number in range(1，11,3)：  # 1-10, step=3
  print(number)
 ```
## exercise1: 
### way1 
```
even_number = 0
for number in range(1,101):
    if number % 2 == 0 : 
        even_number += number 
print(even_number)
```
### way2 
```
even_number = 0
for number in range(1,101,2):
        even_number += number 
print(even_number)
```
## exercise2: 
```
for number in range(1,101):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0 and number % 5 != 0:
        print("Fizz")
    elif number % 3 != 0 and number % 5 == 0:
        print("Buzz")
    else: 
        print(number)
  ```
# 3. Project randomly produce passcode
```
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
```

Eazy Level - Order not randomised:
e.g. 4 letter, 2 symbol, 2 number = JduE&!91
```
code1=""
for i in range(0,nr_letters):             # produce letters randomly
  number_name=random.randint(0,len(letters)-1)     
  i=letters[number_name]
  code1 += i
  
for i in range(0,nr_symbols):            # produce symbols randomly
    number_name=random.randint(0,len(numbers)-1)
    i=numbers[number_name]
    code1 += i
  
for i in range(0,nr_numbers):          # produce numbers randomly
  number_name=random.randint(0,len(symbols)-1)
  i=symbols[number_name]
  code1 += i 
 
print(code1)
```
Hard Level - Order of characters randomised:
e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
```
total_number= nr_letters + nr_symbols + nr_numbers
source = [letters,numbers,symbols]          # nested list,for selecting one data type from letters, symbols and numbers firstly
code2=""
for i in range(0,total_number):
    number_source=random.randint(0,2)       # randomly select one data type from letters, symbols and numbers firstly (for random.randint(1,10), the range is [1,10], but for a list that has 10 items, the index range is [0,9] )
    name_source=source[number_source]       # randomly select one item under the selected data type 
    number_name=random.randint(0,len(name_source)-1)      # or random.choice(name_source) _random.choice()_ randomly select item from a list 
    i=name_source[number_name]
    code2 += i                              # or _code2.append(i)_

print(code2)
```     
