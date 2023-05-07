def get_number(prompt):
    while True:
        try:
            num = float(input(prompt + " "))
            break
        except ValueError:
            print("Invalid input. Try to provide a valid number.")
    return num


def get_operator(prompt):
    while True:
        operator = input(prompt + " ").strip()
        if operator in ('*', '/', '-', '+'):
            break
        else:
            print("You may only enter one of the following operators: + − ∗ /")
    return operator


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    get_number("Please enter a number:")
    get_operator("Please enter an operator:")