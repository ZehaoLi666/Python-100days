# 1.0 Data Types
## 1.1 String 
[] location searching, start from 0 
str() transfer a data type into a string  
```
print("Hello world"[2])
print(str(14321)+str(213213213))  # two string combined with each other 
```
## 1.2 Integer 
121351313
```
print(int("14361635")+int("1")) # transfer a data type into a integer 
name = len(input("what is your name?"))
```
print("you name has" + name + " characters") error: type error name should be a string
```
print(type(name))     # type() look data type
new_name = str(name)  # transfer integer to string 
print("your name has " + new_name + " characters." ) 
```
## 1.3 float
3.1415926
```
float()  # transfer a data type into float 
```
## 1.4 Boolean 
TRUE FALSE


# 2.0 Mathematical Operations 
## 2.1 operations 
```
print(5+3)
print(5-3)
print(5*3)
print(5/5) # when using diving, you will get float even if the results are integer 
print(2 ** 3) # 2的3次方
print(5 % 3) # 5 diveded by 3 , 求余数 modulo 
```
## 2.2 四舍五入 及 保留整数
```
print(round(8/3,2))   # round( ,n) round results , 4舍5入并保留n位小数, but some times it doesn't work 
a = 0.256465465        
print("{:.2f}".format(a))  # equal to round( , n)
print( 8 // 3 )  # = int(8/3)
```
## 2.3+= -= *= /= 
```
a = 1 
a += 1 #  a = a +1 
a -= 1 # a = a -1 
a *=2 # a = a X 2
```
## 2.4 f-string, when using print function, no need to transfer every variables into string  
score =0 
height = 1.8
isWinning = True 
print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")
