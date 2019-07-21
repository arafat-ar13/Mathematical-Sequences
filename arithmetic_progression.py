print("This program simulates an arithmetic progression")

user_choice = input("a) Find the value of a given term")

if user_choice == "a":
    first_term, second_term = input("Enter the first and second term, separated by commas ").split(",")
    first_term, second_term = int(first_term), int(second_term)
    common_difference = second_term - first_term
    user_nth_term = int(input("Enter the term you want the value of: "))
    value_of_nth_term = (first_term) + ((user_nth_term-1) * (common_difference))
    print(f"The value of {user_nth_term}th/nd/st of this series is {value_of_nth_term}")