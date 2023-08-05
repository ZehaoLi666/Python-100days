# Dictionary

### common syntax: 
dictionary = {key: Value}

example: `dictionary={"Bug": "An error in a program that prevents that program from running as expected."}`

Note:use `" "` for keys and Values

### index a dictionsry: 
`dictionary["key"]`

### add item to dictionary
dictionary: `dictionary["new_key_name"] = "New_value"`
   
string: `"string1" + "string2"`
   
list: `list.append()`

### wipe/create a dictionary
`dictionary={}`

### Nest list and dictionary
```
{
   "Key1":[list],
   "Key2":{key2_2:"Value"}  
}
```


# Practice  
### Practice1
Write a program that converts their scores to grades.
```
student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆

#TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

#TODO-2: Write your code below to add the grades to student_grades.👇
for names in student_scores:
    if student_scores[names] > 90 and  student_scores[names] <= 100:    
        student_grades[names] = "Outstanding"
    elif student_scores[names] > 80 and  student_scores[names] <= 90:
        student_grades[names] = "Exceeds Expectations"
    elif student_scores[names] > 70 and  student_scores[names] <= 80:
        student_grades[names] = "Acceptable"
    else :
        student_grades[names] = "Fail"
# 🚨 Don't change the code below 👇
print(student_grades)
```
### Practice2
You are going to write a program that adds to a travel_log. You can see a travel_log which is a List that contains 2 Dictionaries.
```
travel_log = [
{
  "country": "France",
  "visits": 12,
  "cities": ["Paris", "Lille", "Dijon"]
},
{
  "country": "Germany",
  "visits": 5,
  "cities": ["Berlin", "Hamburg", "Stuttgart"]
},
]
#🚨 Do NOT change the code above

#TODO: Write the function that will allow new countries
#to be added to the travel_log. 👇

def add_new_country(country,visits,cities):
    new_country={}
    new_country["country"]=country
    new_country["visits"]=visits
    new_country["cities"]=cities
    travel_log.append(new_country)



#🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

```
### Practice3
```
from replit import clear
#HINT: You can call clear() to clear the output in the console.
from art import logo 
print(logo)

game_status = True 

dictionary={}

while game_status == True :
  names = input("Name?")
  prices = input("Price?")
  dictionary[names] = prices
  Over = input("anyone alse?")
  if Over == "Y":
    clear()
  elif Over == "N":
    game_status = False

max_name=""
max_price=0
for names in dictionary:
  price = int(dictionary[names])
  if max_price < price:
    max_price = price
    max_name=names

print(f'the winner is {max_name} with {max_price}$.')
```
