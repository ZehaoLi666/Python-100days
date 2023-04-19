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
[Reeborg"s world](https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json)
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
for i in range(1,8):
    step()
    i += 1
    if i == 7 : 
        break        # stop loop if meet some condition 
```
