from math import log
print("This is a geometric progression program")

user_choice = input("a) Find the value of a given nth term: \nb) Find the term of a given value")

if user_choice == "a":
    first_term, second_term = input("Enter the first and second terms, separated by commas: ").split(",")
    first_term, second_term = int(first_term), int(second_term)
    comman_ratio = second_term / first_term
    user_nth_term = int(input("Now, enter the term you want the value of: "))
    value_of_nth_term = first_term * (comman_ratio ** (user_nth_term-1))
    print(value_of_nth_term)

if user_choice == "b":
    first_term, second_term = input("Enter the first and second terms, separated by commas: ").split(",")
    first_term, second_term = int(first_term), int(second_term)
    comman_ratio = second_term / first_term
    user_term_value = int(input("Enter the value of the term you want: "))
    term_of_value = (log(user_term_value/first_term)/(log(comman_ratio))) + 1
    print(term_of_value)