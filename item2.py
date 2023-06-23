def calculate_employee_profit(L1, L2, L3):
    # List to store actual profits for each employee
    actual_profit = []
    # List to store annualized profits for each employee
    annualized_profit = []

    for i in range(len(L1)):
        # Monthly income of the employee
        monthly_income = L1[i]
        # Hourly rate of the employee
        hourly_rate = L2[i]
        # Daily allocated hours of the employee
        daily_hours = L3[i]

        # Calculate the employee's wages
        # Daily wage based on hourly rate and allocated hours
        daily_wage = hourly_rate * daily_hours
        # Weekly wage based on daily wage (5 working days)
        weekly_wage = daily_wage * 5
        # Biweekly wage based on weekly wage (2 weeks)
        biweekly_wage = weekly_wage * 2
        # Overtime hours (if more than 8 hours)
        overtime_hours = max(0, daily_hours - 8)
        overtime_rate = hourly_rate * 1.2  # Overtime rate (20% increase)
        # Overtime wage based on overtime hours and rate
        overtime_wage = overtime_hours * overtime_rate
        # Total wage including regular and overtime wages
        total_wage = biweekly_wage + overtime_wage
        total_wage_with_bonus = total_wage + 10  # Total wage with a $10 bonus

        if daily_hours < 4:
            # Add a $5 daily allowance for employees working less than 4 hours
            total_wage_with_bonus += 5

        # Calculate and store actual profit
        actual_profit.append(monthly_income - total_wage_with_bonus)
        # Calculate and store annualized profit
        annualized_profit.append(
            (monthly_income * 12) - (total_wage_with_bonus * 26)
            )
    # Return the lists of actual and annualized profits
    return actual_profit, annualized_profit
