from float_to_int import float_to_int_converter
print("This program simulates an arithmetic progression")

user_choice = input("a) Find the value of a given term \nb) Find the term of a given value \n" )

def find_value(first_term, second_term, common_difference):
    user_nth_term = int(input("Enter the term you want the value of: "))
    value_of_nth_term = (first_term) + ((user_nth_term-1) * (common_difference))
    print(f"The value of {user_nth_term}th/nd/st of this series is {value_of_nth_term}")

def find_term(first_term, second_term, common_difference):
    user_value_of_nth_term = int(input("Enter the value of the term you are looking for: "))
    term_of_value = ((user_value_of_nth_term + common_difference)-first_term) / common_difference
    answer = float_to_int_converter(term_of_value)
    print(f"The value {user_value_of_nth_term} belongs to the term {answer} for this series")

first_term, second_term = input("Enter the first and second term, separated by commas ").split(",")
first_term, second_term = int(first_term), int(second_term)
common_difference = second_term - first_term

if user_choice == "a":
    find_value(first_term, second_term, common_difference)
elif user_choice == "b":
    find_term(first_term, second_term, common_difference)