from float_to_int import float_to_int_converter
from time import sleep
from sympy import solve
from sympy import Eq
from sympy import symbols
print("This program simulates an arithmetic progression")

sleep(0.5)
user_choice = input("a) Find the value of a given term \nb) Find the term of a given value \nc) Find the sum of a series \nd) Find first term and common difference" )

def find_value(first_term, second_term, common_difference):
    user_nth_term = int(input("Enter the term you want the value of: "))
    value_of_nth_term = (first_term) + ((user_nth_term-1) * (common_difference))
    sleep(0.75)
    print(f"The value of {user_nth_term}th/nd/st of this series is {value_of_nth_term}")

def find_term(first_term, second_term, common_difference):
    user_value_of_nth_term = int(input("Enter the value of the term you are looking for: "))
    term_of_value = ((user_value_of_nth_term + common_difference)-first_term) / common_difference
    answer = float_to_int_converter(term_of_value)
    sleep(0.75)
    print(f"The value {user_value_of_nth_term} belongs to the term {answer} for this series")

def find_sum(first_term, second_term, common_difference):
    how_many_terms = int(input("How many terms are in this series?: "))
    sum_of_series = (how_many_terms/2) * ((2*first_term) + ((how_many_terms-1) * common_difference))
    answer = float_to_int_converter(sum_of_series)
    sleep(0.75)
    print(f"The sum of this series is {answer}")

def first_term_and_difference():
    any_term1 = int(input("Enter any term of a series: "))
    any_term1_value = int(input("Enter its value: "))
    any_term2 = int(input("Enter another term of the same series: "))
    any_term2_value = int(input("Enter its value: "))

    a, d = symbols(['a', 'd'])
    system = [
        Eq(a + (any_term1-1)*d, any_term1_value),
        Eq(a + (any_term2-1)*d, any_term2_value)
        ]
    solution = solve(system, [a, d])
    print(f"Here, the first term is {solution[a]} and common difference is {solution[d]}")



sleep(0.75)
if user_choice != "d":
    first_term, second_term = input("Enter the first and second term, separated by commas ").split(",")
    first_term, second_term = int(first_term), int(second_term)
    common_difference = second_term - first_term

if user_choice == "a":
    sleep(0.75)
    find_value(first_term, second_term, common_difference)
elif user_choice == "b":
    sleep(0.75)
    find_term(first_term, second_term, common_difference)
elif user_choice == "c":
    sleep(0.75)
    find_sum(first_term, second_term, common_difference)
elif user_choice == "d":
    sleep(0.75)
    first_term_and_difference()