from math import log
print("This is a geometric progression program")

user_choice = input(
    "a) Find the value of a given nth term \nb) Find the term of a given value \nc) Find the first term and common ratio with other given values \nd) Find the sum of a geometric series \ne) Find the sum to infinity of a geometric series \n")

def float_to_int_converter(float_number):
    if type(float_number) == float:
        if str(float_number)[-1] == "0":
            return int(float_number)
        else:
            return float_number
    else:
        return "The number given is not a float"


def find_value(first_term, second_term):
    comman_ratio = second_term / first_term
    user_nth_term = int(input("Now, enter the term you want the value of: "))
    value_of_nth_term = first_term * (comman_ratio ** (user_nth_term-1))
    answer = float_to_int_converter(value_of_nth_term)
    print(answer)

def find_term(first_term, second_term):
    comman_ratio = second_term / first_term
    user_term_value = int(input("Enter the value of the term you want: "))
    term_of_value = (log(user_term_value/first_term)/(log(comman_ratio))) + 1
    answer = float_to_int_converter(term_of_value)
    print(answer)

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

    print("First term:" + str(a))
    print("Ratio:" + str(r))

def find_sum(first_term, second_term):
    comman_ratio = second_term / first_term
    number_of_terms = int(input("How many terms in this series?: "))
    if comman_ratio < 1:
        sumation = (first_term * (1-(comman_ratio ** number_of_terms))) / (comman_ratio-1)
    elif comman_ratio > 1:
        sumation = (first_term * ((comman_ratio ** number_of_terms)-1)) / (comman_ratio-1)
    answer = float_to_int_converter(sumation)
    print(answer)

def find_sum_to_infinity(first_term, second_term):
    comman_ratio = second_term / first_term
    if comman_ratio > 1:
        print("The sum of infinity series does not exist")
    elif comman_ratio < 1 and comman_ratio > -1:
        sum_to_infinity = first_term / (1-comman_ratio)
    answer = float_to_int_converter(sum_to_infinity)
    print(answer)


first_term, second_term = input("Enter the first and second terms, separated by commas: ").split(",")
first_term, second_term = int(first_term), int(second_term)

if user_choice == "a":
    find_value(first_term, second_term)
elif user_choice == "b":
    find_term(first_term, second_term)
elif user_choice == "c":
    find_first_term_and_ratio()
elif user_choice == "d":
    find_sum(first_term, second_term)
elif user_choice == "e":
    find_sum_to_infinity(first_term, second_term)