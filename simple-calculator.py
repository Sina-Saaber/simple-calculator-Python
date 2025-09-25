def select_operation():
    print("Select a operation to perform >>>")
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. divide")
    print("5. power")
    print("6. radical")

    operation_select = input("Enter operation or its key number : ").lower()
    print()
    return operation_select
 
def convert_int_input(user_input):
    while user_input not in ["", "exit"] :
        try:
            number = float(user_input)
            return number
        except ValueError:
            print("Invalid input!! try a true number...")
            user_input = input("Enter another number: ")

def add_operation():
    result = 0
    user_input = input("Enter Your number: ")
    while user_input not in ["", "exit"] :
        number = convert_int_input(user_input)
        result += number
        user_input = input("Enter another number: ")
    return result

def subtract_operation():
    user_input = 0 
    number = 0
    first_input = input("Enter Your first number: ")
    result = convert_int_input(first_input)
    while user_input not in ["", "exit"] :
        number = convert_int_input(user_input)
        result -= number
        user_input = input("Enter another number: ")
    return result

def multiply_operation():
    result = 1
    user_input = input("Enter Your number: ")
    while user_input not in ["", "exit"] :
        number = convert_int_input(user_input)
        result *= number
        user_input = input("Enter another number: ")
    return round(result, 3)

def divide_operation():
    user_input = 0 # debug-defult
    first_input = input("Enter Your first number: ")
    result = convert_int_input(first_input)
    while user_input not in ["", "exit"] : 
        number = convert_int_input(user_input)
        try:
            result /= number 
        except ZeroDivisionError:
            print("Zero divison error!! try again...")
        user_input = input("Enter another number: ")
    return round(result, 3)

def power_operation():
    result = 1
    first_input = input("Inter your first number: ")
    first_number = convert_int_input(first_input)
    secened_input = input("Inter your secend number (power number): ")
    power = int(convert_int_input(secened_input))
    for i in range(0, power):
        result *= first_number
    return round(result, 3)

def radical_operation():
    user_input = input("Enter Your number: ")
    number = int(convert_int_input(user_input))
    return round((number ** 0.5), 3)
    # i = 0
    # while i < number :
    #     if (number - i*i) < 0.1 :
    #         return round(i, 3)
    #     i += 0.001
    # print("Radical is not defind !!")
        
# main function that do conecting and handeling to other functions
def main_luancher(operation_select):
    print('Type and enter "exit" or just press <enter> for exit')
    if operation_select in ["1", "add"] :
        print(f"Result : {add_operation()}")

    elif operation_select in ["2", "subtract"]:
        print(f"Result : {subtract_operation()}")

    elif operation_select in ["3", "mulitply"] :
        print(f"Result : {multiply_operation()}")

    elif operation_select in ["4", "divide"] :
        print(f"Result : {divide_operation()}")

    elif operation_select in ["5", "power"] :
        print(f"Result : {power_operation()}")
    
    elif operation_select in ["6", "radical"] :
        print(f"Result : {radical_operation()}")

    else:
        print("Invalid input!! try again...")
        main_luancher(select_operation())

main_luancher(select_operation())