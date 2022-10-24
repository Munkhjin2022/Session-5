
response=str(input("Do you want to continue? (Yes or No) "))

while (response== "Yes"):
  name=str(input("Please enter the last name "))
  Sc1=float(input("Please enter exam score 1 "))
  Sc2=float(input("Enter exam score 2 "))

  avage=(Sc1 + Sc2)/2

  print("Name: ", name)
  print("The exam score 1: ", Sc1)
  print("Score 2: ", Sc2)
  print("The average exam score: ", avage)

  response=str(input("Do you want to continue? (Yes or No) ")) 
