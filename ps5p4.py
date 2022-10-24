#comment input
counter=0
totalgross=0.0

response=str(input("Do you want to continue? (Yes or No)"))
#process phase
while response=="Yes":
  counter=counter+1
  name=str(input("Enter name"))
  hours=float(input("Enter number of hours worked "))
  rate=float(input("Enter rate of pay"))

  if hours>40:
    grosspay=(hours-40)*rate*1.5+(40*rate)
  else:
    grosspay=hours*rate

  totalgross=totalgross+grosspay

  print("Name: ", name)
  print("Gross pay: ", grosspay)

  response=input("Do you want to continue? (Yes or No)")

#output
  avgross=totalgross/counter

print("Number of employees: ", counter)
print("Total gross pay: ", totalgross)
print("Average pay: ",avgross)

