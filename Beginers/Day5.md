# for loop 
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
# range()
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
## exercise3: 
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
