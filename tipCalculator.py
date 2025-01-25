## Create a tip calculator.##
#
## Welcome Message.##
print("Welcome to the bill/tip calculator!")
#
## Let's ask the user some questions with our code.##
#
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage of tip would you like to give? 10, 12, 15 Just give the number"))
people = int(input("How many people are goint to split the bill?" )) 
#
## Now we will calculate everything.##
#
total_bill = tip / 100 * bill + bill
bill_per_person = total_bill / people
final_amount = round(bill_per_person, 2)
#
## Let's give the user the total.##
print(f"Your bill total is ${bill}. You would like to tip {tip}%. Your total is ${total_bill}. The amount to split per person is ${final_amount}.")
#
# end
