#Tip calculator
print("Welcome to tip calculator")
bill = float (input("how much is the bill?"))
tip = int(input("what percentage of tip will you give 10%,15%, 18%?"))
people = int(input("how many people are there?"))

bill_with_tip = tip / 100 * bill + bill
bill_with_tip_people = bill_with_tip / people
print(f"every one should pay $ {bill_with_tip_people}")
