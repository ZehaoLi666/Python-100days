y# get two random cards
import random 
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
dealer_number1 = int(random.choice(cards))
dealer_number2 = int(random.choice(cards))
dealer_number=[dealer_number1,dealer_number2]
dealer_add=dealer_number1+dealer_number2
print(f"Dealer number is {dealer_add}")

User_number1 = int(random.choice(cards))
User_number2 = int(random.choice(cards))
User_number=[User_number1,User_number2]
User_add = User_number1+User_number2
print(f"User number is {User_add}")

loop_stop = False
game_over = False
while loop_stop == False:

# No Blackjacks
  if dealer_add == 21 and User_add != 21:
    print('Dealer win')
  if dealer_add != 21 and User_add == 21:
    print('User win')
  if dealer_add == 21 and User_add == 21:
    print("Draw")

# Is user's score over 21 
  if User_add > 21:
    for number in User_number:
      if number == 11:
        number = 1 
        User_add += number               # HERE MAY HAS A PROBLEM
    if User_add > 21: 
      print(f"User number is {User_add},User lose")
      loop_stop = True
      game_over = True
    else:
      add_card=input("Do you want to get another card? Y or N? ")
      if add_card == "Y":
        add_number = int(random.choice(cards))
        User_add += add_number
      else:
         loop_stop = True
        
  else:
    add_card=input("Do you want to get another card? Y or N? ")
    if add_card == "Y":
      add_number = int(random.choice(cards))
      User_add += add_number
      print(f"User number is {User_add}")
    else:
       loop_stop = True

if game_over == False:
 computer_loop = True
 while computer_loop:
   if dealer_add < 17:
     add_number = int(random.choice(cards))
     dealer_add += add_number
     if dealer_add > 21:
       print(f"dealer numebr is {dealer_add}, dealer win.")
       computer_loop = False
       game_over = True
   else:
      if dealer_add > User_add:
        print("dealer win")
        computer_loop = False
      elif dealer_add < User_add : 
        print("User win")
        computer_loop = False
      else:
        print("Draw")
        computer_loop = False
