# 1.0 operators 
## > < >= <= == != 

# 2.0 if else examples:
## 2.1 example1
```
print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))

if height >= 120 : 
  print("You can ride the rollercoaster!")
else: 
  print("You can not ride rollercoaster!")
```
# 2.2 example2: 
```
number = int(input("Which number do you want to check? "))
number1 = number % 2 

if number1 == 0: 
    print("This is an even number.")
else : 
    print("This is an odd number.")
```
# 3.0 nested ifelse and if elif else :
```
if height >= 120 : 
  print("You can ride the rollercoaster!")
  age = int(input("What is your age?"))
  if age <= 12: 
    print("Plsease pay $5.")
  elif age <= 18: 
    print("Please pay $7")
  elif age <= 60:
    print("Please pay $12")
  else: 
    print("please pay $5")
else: 
  print("You can not ride rollercoaster!")
```
## 3.1 example1 if elif else
```
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))


bmi = weight / height ** 2
bmi = float("{:.2}".format(bmi))     
if bmi <= 18.5: 
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi <= 25: 
    print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi <= 30: 
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi <= 35: 
    print(f"Your BMI is {bmi}, you are obese.")
else:
    print(f"Your BMI is {bmi}, you are clininally obese.")
```
## 3.2 example 2: nested ifelse
### 3 levels nested ifelse
```
year = int(input("Which year do you want to check? "))

if year % 4 ==0: 
    if year % 100 ==0 : 
        if year % 400 ==0: 
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else: 
    print("Not leap year.") 
```
# 4.0 Multiple if 
```
if condition1: 
   A 
 if cindition2:
   B
 同时成立，同时输出AB
``` 
```
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")


if size == "S": 
    bill = 15
    if  add_pepperoni == "Y":
        bill += 2
    if extra_cheese == "Y":
        bill += 1  
elif size == "M":
    bill = 20
    if  add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1 
else :
    bill = 25
    if  add_pepperoni == "Y":
        bill += 3
    if extra_cheese == "Y":
        bill += 1 

print (f"Your final bill is: ${bill}.")
```
# 5.0 logic operators 
 and or not : combine two conditions together 
 name.lower() lower case the string   name.count("n") count the number of character in a string
```
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")


name1=name1.lower() 
name2=name2.lower()

number1 = name1.count("t") + name1.count("r") + name1.count("u") + name1.count("e") +  name2.count("t") + name2.count("r") + name2.count("u") + name2.count("e")
number2 = name1.count("l") + name1.count("o") + name1.count("v") + name1.count("e") +  name2.count("l") + name2.count("o") + name2.count("v") + name2.count("e")

number3 = str(number1) + str(number2)
number3 = int(number3)
if number3 < 10 or number3 > 90: 
    print(f"Your score is {number3}, you go together like coke and mentos.")
elif number3 >=40 and number3 <= 50: 
    print(f"Your score is {number3}, you are alright together.")
else: 
    print(f"Your score is {number3}.")
```
