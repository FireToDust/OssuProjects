MONTH = 1
MONTHS_IN_YEAR = 12
PORTION_DOWN_PAYMENT = 0.25
R = 0.04
MONTHLY_RATE = R / MONTHS_IN_YEAR


def house_hunt(annual_salary, portion_saved, total_cost):
    """
    This function returns how long it would take to save up to get a house, for the specific case of
    the OSSU Problem Set 1, problem A.

    Arguments:
    :param annual_salary:  your annual salary
    :param portion_saved:  how much of your income you save
    :param total_cost:     cost of the house your saving up for
    :return:               time to get a down payment
    """

    def time_to_save(goal, multiplier, adder, total=0, time=0):
        # returns how long it would take for a number to get to goal, where every unit of time the number (starting
        # at 0) is multiplied by 1 + the multiplier then incremented with the adder.

        if total >= goal:
            return time

        newTotal = total * (1 + multiplier) + adder

        return time_to_save(goal, multiplier, adder, newTotal, time+1)

    salary_saved = (annual_salary/MONTHS_IN_YEAR) * portion_saved
    down_payment_cost = total_cost*PORTION_DOWN_PAYMENT

    return time_to_save(down_payment_cost, MONTHLY_RATE, salary_saved)


def test_house_hunt():
    """
    Tests house hunt function and throws an error if a test case fails

    :return:  True
    """

    assert house_hunt(120000, 0.10, 1000000) == 183, "House Hunt Test Case 1 failed"
    assert house_hunt(80000, 0.15, 500000) == 105, "House Hunt Test Case 2 failed"

    return True

