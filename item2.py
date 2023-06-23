def calculate_employee_profit(L1, L2, L3):
    actual_profit = []  # List to store actual profits for each employee
    annualized_profit = []  # List to store annualized profits for each employee

    for i in range(len(L1)):
        monthly_income = L1[i]  # Monthly income of the employee
        hourly_rate = L2[i]  # Hourly rate of the employee
        daily_hours = L3[i]  # Daily allocated hours of the employee

        # Calculate the employee's wages
        daily_wage = hourly_rate * daily_hours  # Daily wage based on hourly rate and allocated hours
        weekly_wage = daily_wage * 5  # Weekly wage based on daily wage (5 working days)
        biweekly_wage = weekly_wage * 2  # Biweekly wage based on weekly wage (2 weeks)
        overtime_hours = max(0, daily_hours - 8)  # Overtime hours (if more than 8 hours)
        overtime_rate = hourly_rate * 1.2  # Overtime rate (20% increase)
        overtime_wage = overtime_hours * overtime_rate  # Overtime wage based on overtime hours and rate
        total_wage = biweekly_wage + overtime_wage  # Total wage including regular and overtime wages
        total_wage_with_bonus = total_wage + 10  # Total wage with a $10 bonus

        if daily_hours < 4:
            total_wage_with_bonus += 5  # Add a $5 daily allowance for employees working less than 4 hours

        actual_profit.append(monthly_income - total_wage_with_bonus)  # Calculate and store actual profit
        annualized_profit.append((monthly_income * 12) - (total_wage_with_bonus * 26))  # Calculate and store annualized profit
    return actual_profit, annualized_profit  # Return the lists of actual and annualized profits
