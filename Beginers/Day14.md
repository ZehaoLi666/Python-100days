# practice(by myself)
# when use global variants in a function, use global, when output a global variant, use return
```
import random
from game_data import data
game_over= 1 
def generateA():
  number = random.randint(1,49)
  return number
def generateB():
  breaka=False
  while not breaka:
    number = random.randint(1,49)
    global A
    if number != A :
      breaka = True
      return number

def compare(numberA,numberB):
  global SCORE
  global game_over
  if guess=="A": 
    if numberA > numberB: 
      SCORE += 1
      print(f"You are right! Current score is {SCORE}.")
      compareA=data[B]
      print(f"compare A: {compareA['name']}, a {compareA['description']},from {compareA['country']}.")

    if numberA < numberB: 
      
      game_over = 2
      print(f"Sorry, that's wrong. Final score:{SCORE}.")
      return game_over
  if guess=="B":
    if numberA > numberB:
      
      game_over = 2
      print(f"Sorry, that's wrong. Final score:{SCORE}.")
      return game_over
    if numberA < numberB: 
      SCORE += 1
      print(f"You are right! Current score is {SCORE}.")
      compareA=data[B]
      print(f"compare A: {compareA['name']}, a {compareA['description']},from {compareA['country']}.")
    




from art import logo 
from art import vs

print(logo)
SCORE=0

A = generateA()
compareA=data[A]
print(f"compare A: {compareA['name']}, a {compareA['description']},from {compareA['country']}.")
while  game_over == 1:
  B = generateB()    
  compareB=data[B]
  print(vs)
  print(f"compare B: {compareB['name']}, a {compareB['description']},from {compareB['country']}.")

  guess=input("Who has more followers? Type A or B: ")
  numberA=int(compareA['follower_count'])
  numberB=int(compareB['follower_count'])
  compare(numberA,numberB)

```
