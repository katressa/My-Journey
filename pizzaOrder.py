#!python3
print("Welcome to Python Pizza deliveries")
#size = input("What size pizza would you like? S, M, L:")
#pepperoni = input("Would you like pepperoni on your pizza? Y or N:")
#extra_chesse = input("Would you like extra cheese? Y or N: ")

#Work out how much they need to pay based on their size.
#
size = input("What size pizza would you like? S, M, L:")
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25
print(size)
#Work out how much they need to pay based on their pepperoni choice.
#
pepperoni = input("Would you like pepperoni on your pizza? Y or N:")
if pepperoni == "Y":
    bill = bill + 2
elif pepperoni == "N":
    print("No pepperoni, what a bummer") 
#
#Work out how much they need to pay based on their extra cheese choice.
extra_chesse = input("Would you like extra cheese? Y or N: ")
if extra_chesse == "Y":
    bill = bill + 1
elif extra_chesse == "N":
    print("No cheese, please! ")

print(f"Your final bill is ${bill}.")
#end
