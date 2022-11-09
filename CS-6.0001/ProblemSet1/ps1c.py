import math
import os

portion_down_payment = 0.25
r = 0.04
monthly_rate = r / 12
MONTHS_IN_YEAR = 12
MONTH = 1
TOTAL_COST = 1000000
RAISE = 0.07
SAVE_TIME = 36


def aprox_equal(num1, num2, precision):
    """
    Returns if num1 and num2 are within precision of each other
    :param num1:       first number
    :param num2:       second number
    :param precision:
    :return:
    """
    return -precision <= num1 - num2 <= precision


def bisection_search(func, goal, check_precision, unit_size, minimum, maximum):


    def recursion(minimum1, maximum1, iterations):
        if minimum1 == maximum1:
            # returns false if the goal is not in the range minimum to maximum
            return False

        mid = (minimum1 + maximum1) / 2

        test = func(mid * unit_size)

        if aprox_equal(goal, test, check_precision):
            return mid * unit_size
        elif test > goal:
            return recursion(minimum1, math.floor(mid), iterations + 1)
        else:
            return recursion(math.ceil(mid), maximum1, iterations + 1)

    return recursion(math.floor(minimum / unit_size), math.ceil(maximum / unit_size), 0)


def preset_function(*args):
    """
    dec
    :param func:
    :return:
    """

    def inner(func):
        def wrapper(*args2):
            none_count = args.count(None)
            arg_length = len(args2)

            assert arg_length == none_count, (wrapper.__name__ + "(*args) takes "
                                              + str(none_count) + " positional arguments but "
                                              + str(arg_length) + " were given")

            iterator = iter(args2)

            def replace_none(inp):
                if inp is None:
                    return next(iterator)
                return inp

            new_args = map(replace_none, args)

            return func(*new_args)

        return wrapper

    return inner


def saving_with_raise(annual_salary):
    """
    saving_with_raise(annual_salary)

    This function returns how much of your income you would have to save to get a certain amount of money in three
    years, for the specific case of the OSSU Problem Set 1, problem C.

    Arguments:
    :param annual_salary:  your annual salary
    :return:               income portion to save
    """

    down_payment_cost = TOTAL_COST * portion_down_payment
    monthly_salary = annual_salary/12

    @preset_function(SAVE_TIME, monthly_rate, None, RAISE, MONTHS_IN_YEAR / 2)
    def money_after_time(time, multiplier, adder, adder_multiplier, period):
        # returns how long it would take for a number to get to goal, where every unit of time the number (starting
        # at 0) is multiplied by 1 + the multiplier then incremented with the adder.
        # the adder is also multiplied by adder_multiplier every period amount of time

        # I have inner recursion so my decorator doesn't mess with it
        def recursion(total, iterations):
            if iterations >= time:
                return total

            currentAdder = adder * (1+adder_multiplier)**math.floor(iterations/period)

            newTotal = total * (1 + multiplier) + currentAdder
            return recursion(newTotal, iterations + 1)
        return recursion(0, 0)

    money_after_time = preset_function(SAVE_TIME, monthly_rate, None, RAISE, MONTHS_IN_YEAR / 2)(money_after_time)
    money_after_time(1)

    incomeRequired = bisection_search(money_after_time, down_payment_cost, 100, 0.001, 0, monthly_salary)

    # the function returns false if you cant save up enough in 3 years
    if not incomeRequired:
        return False

    portion_required = incomeRequired / monthly_salary
    return portion_required


def test_saving_with_raise():
    """
    Throws an error if a test case fails

    :return: True
    """

    return True


salary = 10000
print(salary / 12)
print(saving_with_raise(salary))
