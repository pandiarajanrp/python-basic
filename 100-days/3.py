#Conditional Statements,

#if

age=int(input("Enter your age "))


if not age == 0:
  if age >= 18:
    print("You are adult")
  elif age > 15 and age < 18:
    print("You are about to an adult")
  elif age > 10 or age > 12:
    print("you are above child")
  else:
    print("you are child")
else:
  print("there is no person with age 0")