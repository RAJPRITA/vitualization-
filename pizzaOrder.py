print("Welcome to pizza order dilivary")

size = input("What is the size of piza you need ? S,M,L")
add_pepporoni = input("Do you want pepporoni? Y OR N")
extra_cheese = input("do you want extra cheese")

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
else:
    bill = 25

if add_pepporoni =="Y":
    bill +=2
if extra_cheese == "Y":
    bill +=1

print(f"Your final bill is {bill}")
