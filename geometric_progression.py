from math import log
from time import sleep
from float_to_int import float_to_int_converter
print("This is a geometric progression program")

sleep(1)
user_choice = input(
    "a) Find the value of a given nth term \nb) Find the term of a given value \nc) Find the first term and common ratio with other given values \nd) Find the sum of a geometric series \ne) Find the sum to infinity of a geometric series \n")


def find_value(first_term, second_term, common_ratio):
    user_nth_term = int(input("Now, enter the term you want the value of: "))
    term_of_value = first_term * (common_ratio ** (user_nth_term-1))
    answer = float_to_int_converter(term_of_value)
    sleep(0.5)
    print(f"The value of {user_nth_term}(th/nd/st) term for this series is {answer}")

def find_term(first_term, second_term, common_ratio):
    user_term_value = int(input("Enter the value of the term you want: "))
    term = (log(user_term_value/first_term)/(log(common_ratio))) + 1
    answer = float_to_int_converter(term)
    sleep(0.5)
    print(f"The value {user_term_value} belongs to the {answer}(th/nd/st) term")

def find_first_term_and_ratio():
    any_term1 = int(input("Enter the term "))
    any_term1_value = int(input("Enter its value: "))

    any_term2 = int(input("Enter the term "))
    any_term2_value = int(input("Enter its value: "))

    term_difference = any_term1 - \
        any_term2 if any_term1 > any_term2 else any_term2 - any_term1
    b, c = (any_term1_value, any_term2_value) if any_term1_value > any_term2_value else (
        any_term2_value, any_term1_value)

    r = int((b / c) ** (1/term_difference))
    a = int(any_term1_value / (r ** (any_term1 - 1)))
    
    sleep(0.5)
    print("First term:" + str(a))
    print("Ratio:" + str(r))

def find_sum(first_term, second_term, common_ratio):
    number_of_terms = int(input("How many terms in this series?: "))
    if common_ratio < 1:
        sumation = (
            first_term * (1-(common_ratio ** number_of_terms))) / (common_ratio-1)
    elif common_ratio > 1:
        sumation = (
            first_term * ((common_ratio ** number_of_terms)-1)) / (common_ratio-1)
    answer = float_to_int_converter(sumation)
    sleep(0.5)
    print(f"The sum of this series is {answer}")

def find_sum_to_infinity(first_term, second_term, common_ratio):
    if common_ratio > 1:
        print("The sum of infinity series does not exist")
    elif common_ratio < 1 and common_ratio > -1:
        sum_to_infinity = first_term / (1-common_ratio)
    answer = float_to_int_converter(sum_to_infinity)
    sleep(0.5)
    print(f"The sum to infinity of this series is {answer}")

sleep(1)
if user_choice != "c":
    first_term, second_term = input("Enter the first and second terms, separated by commas: ").split(",")
    first_term, second_term = int(first_term), int(second_term)
    common_ratio = second_term / first_term

if user_choice == "a":
    sleep(1)
    find_value(first_term, second_term, common_ratio)
elif user_choice == "b":
    sleep(1)
    find_term(first_term, second_term, common_ratio)
elif user_choice == "c":
    sleep(1)
    find_first_term_and_ratio()
elif user_choice == "d":
    sleep(1)
    find_sum(first_term, second_term, common_ratio)
elif user_choice == "e":
    sleep(1)
    find_sum_to_infinity(first_term, second_term, common_ratio)