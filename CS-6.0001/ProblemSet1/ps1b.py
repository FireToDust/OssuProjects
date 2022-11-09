import math

portion_down_payment = 0.25
r = 0.04
monthly_rate = r / 12
MONTHS_IN_YEAR = 12
MONTH = 1


def saving_with_raise(annual_salary, portion_saved, total_cost, _raise):
    """
    saving_with_raise(annual_salary, portion_saved, total_cost, _raise)

    This function returns how long it would take to save up to get a sertan amount of money, for the specific case of
    the OSSU Problem Set 1, problem B.
    Arguments:
    :param annual_salary:  your annual salary
    :param portion_saved:  how much of your income you save
    :param total_cost:     cost of the house your saving up for
    :param _raise:         a raise you get every half a year
    :return:               time to get a down payment
    """

    def time_to_save(goal, multiplier, adder, adder_multiplier, period, total=0, time=0):
        # returns how long it would take for a number to get to goal, where every unit of time the number (starting
        # at 0) is multiplied by 1 + the multiplier then incremented with the adder.
        # the adder is also multiplied by adder_multiplier every period amount of time

        if total >= goal:
            return time

        newAdder = adder
        if time % period == 0 and time != 0:
            newAdder *= 1+adder_multiplier

        newTotal = total * (1 + multiplier) + newAdder

        return time_to_save(goal, multiplier, newAdder, adder_multiplier, period, newTotal, time + 1)

    salary_saved = annual_salary * portion_saved / MONTHS_IN_YEAR
    down_payment_cost = total_cost * portion_down_payment
    return time_to_save(down_payment_cost, monthly_rate, salary_saved, _raise, MONTHS_IN_YEAR / 2)


def test_saving_with_raise():
    """
    Throws an error if a test case fails

    :return: True
    """

    assert saving_with_raise(120000, 0.05, 500000, 0.03) == 142, "Saving With a Raise Test Case 1 failed"
    assert saving_with_raise(80000, 0.10, 800000, 0.03) == 159, "Saving With a Raise Test Case 2 failed"
    assert saving_with_raise(75000, 0.05, 1500000, 0.05) == 261, "Saving With a Raise Test Case 3 failed"

    return True


print(test_saving_with_raise())
