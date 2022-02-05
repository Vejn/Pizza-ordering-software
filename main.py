# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#First checking the size of pizza
#In case of small pizza
if size.lower() == 's':
  price = 15
  #Checking if add_pepperoni True
  if add_pepperoni.lower() == 'y':
    price += 2
#In case of medium pizza
elif size.lower() == 'm':
  price = 20
  #Add pepperoni?
  if add_pepperoni.lower() == 'y':
    price += 3
else:
  #If size don't apply, we sell largest pizza
  price = 25
  #Add pepperoni?
  if add_pepperoni.lower() == 'y':
    price += 3
#Extra cheese?
if extra_cheese.lower() == 'y':
  price += 1
#Print final bill
print(f"Your final bill is: ${price}")





