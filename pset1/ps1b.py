# MIT 6.001 pset 1b

total_cost = 0.0
portion_down_payment = 0.25
total_down_payment = 0.0
current_savings = 0.0
r = 0.04
annual_sallary = 0.0
portion_saved = 0.0
semi_annual_raise = 0.0
months = 0

total_cost = float(input("Whats the cost of the house? "))
annual_sallary = float(input("Whats your annual sallary? "))
portion_saved = float(input("Portion of the sallary to be saved? "))
semi_annual_raise = float(input("Whats your semi annual raise? "))

total_down_payment = total_cost * portion_down_payment

while current_savings < total_down_payment:
    if months != 0 and months % 6 == 0:
        annual_sallary += annual_sallary * semi_annual_raise
    months += 1
    current_savings += (annual_sallary * (portion_saved/12) + (current_savings * r/12))

print("it will take", months, "months")

