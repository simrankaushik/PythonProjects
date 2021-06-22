# tip calculator

print("welcome to the tip calculator")
total_bill=float(input("what is your total bill: "))
tip=int(input("what percentage tip would u like to give(10,12 or 15): "))
spliting= int(input("how many people to split the bill: "))

bill_with_tip = tip/100 * total_bill + total_bill
final_amount = round(bill_with_tip,2)
bill_per_person = final_amount / spliting
print(bill_per_person)
