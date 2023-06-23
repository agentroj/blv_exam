import pytest
# Import the function
from item2 import calculate_employee_profit


# Scenario 1: Basic input values
def test_calculate_employee_profit_basic():
    L1 = [5000, 6000, 7000]
    L2 = [20, 25, 30]
    L3 = [8, 8, 8]
    actual_profits, aoia_profits = calculate_employee_profit(L1, L2, L3)
    assert actual_profits == [3390, 3990, 4590]
    assert aoia_profits == [18140.0, 19740.0, 21340.0]


# Scenario 2: Varying hours and rates
def test_calculate_employee_profit_varying_hours_rates():
    L1 = [4000, 4500, 6000]
    L2 = [15, 18, 20]
    L3 = [6, 9, 10]
    actual_profits, aoia_profits = calculate_employee_profit(L1, L2, L3)
    assert actual_profits == [3090, 2848.4, 3942.0]
    assert aoia_profits == [24340.0, 11058.400000000001, 18492.0]


# Scenario 3: Overtime and daily allowance
def test_calculate_employee_profit_overtime_allowance():
    L1 = [8000, 9000, 10000]
    L2 = [25, 30, 35]
    L3 = [9, 10, 11]
    actual_profits, aoia_profits = calculate_employee_profit(L1, L2, L3)
    assert actual_profits == [5710.0, 5918.0, 6014.0]
    assert aoia_profits == [36460.0, 27868.0, 16364.0]


# Scenario 4: Low hours and allowance
def test_calculate_employee_profit_low_hours_allowance():
    L1 = [3000, 3500, 4000]
    L2 = [10, 12, 15]
    L3 = [4, 5, 6]
    actual_profits, aoia_profits = calculate_employee_profit(L1, L2, L3)
    assert actual_profits == [2590, 2890, 3090]
    assert aoia_profits == [25340.0, 26140.0, 24340.0]


# Scenario 5: Combined scenarios
def test_calculate_employee_profit_combined():
    L1 = [7000, 7500, 8000]
    L2 = [22, 26, 28]
    L3 = [8, 9, 10]
    actual_profits, aoia_profits = calculate_employee_profit(L1, L2, L3)
    assert actual_profits == [5230, 5118.8, 5122.8]
    assert aoia_profits == [37980.0, 28088.800000000003, 21192.800000000003]
