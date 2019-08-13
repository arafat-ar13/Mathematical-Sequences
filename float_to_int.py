def float_to_int_converter(float_number):
    if type(float_number) == float:
        if str(float_number)[-1] == "0":
            return int(float_number)
        else:
            return float_number
    else:
        return "The number given is not a float"

floating_num = float(input("enter number: "))
print(float_to_int_converter(floating_num))