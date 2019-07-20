print("This is a geometric progression program")

user_choice = input("a) Find the value of a given nth term: ")

if user_choice == "a":
    first_term, second_term = input("Enter the first and second terms, separated by commas: ").split(",")
    first_term, second_term = int(first_term), int(second_term)
    comman_ratio = second_term / first_term
    user_nth_term = int(input("Now, enter the term you want the value of: "))
    value_nth_term = first_term * (comman_ratio ** (user_nth_term-1))
    print(value_nth_term)