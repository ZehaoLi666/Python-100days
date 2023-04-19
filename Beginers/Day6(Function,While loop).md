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
```
whil some condition is true: 
    Do some thing repeatly
```
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
# 4. difference between for in loop and while loop 
* for in loop: to run based on finite times that you know 
* while: to run based on condition, so you don't know how many times it will run 
   
