# 1. Function 
## 1.1 Defining a function
```
def function_name():
    print("Hello")
    print("Bye")
```
## 1.2Calling a function 
```
function_name()
```
## 1.3 practice1 
[Reeborg"s world1](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json)
```
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def step():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

i = 0    
for i in range(1,7):
    step()
```
or 
```
for i in range(60):
    step()
```
# 2. Indentation 
 [Indentation](https://peps.python.org/pep-0008/)
 
# 3. While Loop
## 3.1 while loop
```
whil some condition is true: 
    Do some thing repeatly
```
## 3.2 practice2 
[Reeborg"s world2](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%202&url=worlds%2Ftutorial_en%2Fhurdle2.json)
```
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def step():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

   
while at_goal() != True: 
    step()
```   
way2
```
while not at_goal(): 
    step()
```
## 3.3 ifference between for in loop and while loop 
* for in loop: to run based on finite times that you know 
* while loop: to run based on condition, so you don't know how many times it will run 
* If you want to iterate a list and you want to do something to each item in the list, use for in loop.
* If you only want to repeat some functions until it meet a condition and you don't care about which item you are iterating(do something for each item), use while loop. Be careful of it, because it may run forever, if it doesn't meet the condition you want.

## 3.4 practice 3 
[Reeborg"s world3](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%203&url=worlds%2Ftutorial_en%2Fhurdle3.json)
```
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

   
while at_goal() != True: 
    if front_is_clear():
        move()
    if  wall_in_front(): 
        jump()
```
## 3.5 practice 4 
[Reeborg"s world4](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%204&url=worlds%2Ftutorial_en%2Fhurdle4.json)
```
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()    
    while not right_is_clear():       
        move()
    turn_right()
    move()
    turn_right()
    while not wall_in_front():
        move()
    turn_left() 
    
while not at_goal():
    if front_is_clear():
        move()
    if wall_in_front():
        jump()
```
