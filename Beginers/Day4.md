# 1.0 random dunction 
[Askpython-random methods](https://www.askpython.com/python-modules/python-random-module-generate-random-numbers-sequences)
## 1.1 random.randint()
```
import random
a = random.randint(1,10)     # 随机生成整数
print(a)
b = random.random()          # 随机生成[0,1)的float
print(b)
c = random.uniform(1,10)     # [1,10] float 
print(c)
```
## 1.2 module  
```
import script.py  /   import package
```
## 1.3 exercise 1
You are going to write a virtual coin toss program. It will randomly tell the user "Heads" or "Tails".
```
import random	 

random_number = random.randint(1,10) 
random_number2 = random_number % 2

if random_number2 == 0:
    print("Heads")
else: 
    print("Tails")
```
# 2.0 List
## 2.1 build a list and subcut 
```
fruits = ["apple","cherry","Pear"]    # build a list 
print(fruits[0])                      # subcut a list (use positive index)
print(fruits[-1])                     # subcut a list (use negative index: strat at the end of the list)
fruits[1] = "yingtao"                 # revise the list    
print(fruits)

fruits.append("watermalon")           # add a item at the end of the list 
print(fruits)

fruits.extend(["mango","dragon fruit"])  # add a list to a given list
print(fruits)
```
## 2.2 split( ) function  split a string into separate compents 
```
string = "sdjhf,sdjhfgdsj,sdihgfhjds,sjhgfj"
list = string.split(",")              # split the string by , and transfer it into a list 
print(list)
```

## 2.3 exercise 2: randomly select a item in the list
```
names_string = "Angela, Ben, Jenny, Michael, Chloe"
names = names_string.split(", ")
number1 =len(names)     # number of items in the list 
import random
number2 = random.randint(0 , number1 - 1)
name = names[number2]
print(f"{name} is going to buy the meal today!")
name = random.choice(names)                        # random.choice() is equal to previous command lines
print(name + " is going to buy the meal today!")
```

# 3.0 Nested list 
## 3.1 list1 = [list2,list3]
```
fruits = ["Apple","Watermalon"]
vegatable = ["Carrot","Chili"]
food = [fruits,vegatable]
print(food)
print(food[1][1])  # No.2 list No.2 item  
```
## 3.2 exercise 3 
replace one of these "⬜️" by 'X', when you type column and row number 
```
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

column_number = int(position[0])
row_number = int(position[1])

map[row_number - 1][column_number -1] = 'X'

print(f"{row1}\n{row2}\n{row3}")
```
# 4.0 Project

