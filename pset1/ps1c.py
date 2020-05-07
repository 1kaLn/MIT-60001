# MIT 6.001 pset 1c

total_cost = 1000000.0
portion_down_payment = 0.25
total_down_payment = total_cost * portion_down_payment
current_savings = 0.0
r = 0.04
base_annual_sallary = 0.0
semi_annual_raise = 0.07
best_saving_rate = 0.0
money_range = 100.0
months = 36
init_upper = 10000
upper_bound = init_upper
lower_bound = 0
portion_saved = (upper_bound + lower_bound) / 2
steps = 0

base_annual_sallary = float(input("Whats your annual sallary? "))

while abs(current_savings - total_down_payment) > money_range:
    steps += 1
    current_savings = 0.0
    annual_sallary = base_annual_sallary
    monthly_salary = annual_sallary / 12
    monthly_deposit = monthly_salary * (portion_saved / 10000)

    for month in range(1, months + 1):
        current_savings += current_savings * (r/12)
        current_savings += monthly_deposit

        if month % 6 == 0:
            annual_sallary += annual_sallary * semi_annual_raise
            monthly_salary = annual_sallary / 12
            monthly_deposit = monthly_salary * (portion_saved / 10000)

    prev_portion_saved = portion_saved

    if current_savings > total_down_payment:
        upper_bound = portion_saved
    else:
        lower_bound = portion_saved

    portion_saved = int(round((upper_bound + lower_bound) / 2))

    if prev_portion_saved == portion_saved:
        break

if prev_portion_saved == portion_saved and portion_saved == init_upper:
    print("it is not possible to pay the house in three years")
else:
    print("Best savings rate is", portion_saved / 10000)
    print("Steps in bisection search:", steps)
            
