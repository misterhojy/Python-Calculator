def get_number(prompt):
    while True:
        try:
            num = input(prompt)
            if "+" in num or "." in num:
                raise ValueError
            num = float(num)
            break
        except ValueError:
            print("Invalid input. Try to provide a valid number.")
    return num


def get_operator(prompt):
    while True:
        operator = input(prompt).strip()
        if operator in ('*', '/', '-', '+'):
            break
        else:
            print("You may only enter one of the following operators: + − ∗ /")
    return operator


def halt(prompt):
    while True:
        boolli = input(prompt).strip().lower()
        if boolli in ("y", "yes"):
            return True
        if boolli in ("n", "no"):
            return False
        else:
            print("Invalid response. Please enter [Y|N].")


class Calculator:
    def __init__(self, num1_prompt="Enter the first number: ", operator_prompt="Enter the operator: ",
                 num2_prompt="Enter the second number: ", goodbye_msg=None):
        self.__num1prompt = num1_prompt
        self.__operator_prompt = operator_prompt
        self.__num2prompt = num2_prompt
        self.__goodbye_msg = goodbye_msg

    def calculate(self):
        x = int(get_number(self.__num1prompt))
        opp = get_operator(self.__operator_prompt)
        y = int(get_number(self.__num2prompt))
        z = None
        if opp == '+':
            z = x + y
        if opp == '-':
            z = x - y
        if opp == '*':
            z = x * y
        if opp == '/':
            if y != 0:
                z = x / y
            else:
                print("Can't divide by zero")
            z.__float__()
        if z is not None:
            print("{0:g} {1} {2:g} = {3:.1f}".format(x, opp, y, z))
        return z

    def run(self):
        answers = []
        while True:
            result = self.calculate()
            if result is not None:
                answers.append(result)
            if not halt("Would you like to continue? [Y|N]: "):
                break
        c = "calculations" if len(answers) > 1 else "calculation"
        print(f"You carried out {len(answers)} {c}. The results were {'; '.join([f'{x:.1f}' for x in answers])}")
        if self.__goodbye_msg is not None:
            print(self.__goodbye_msg)


if __name__ == '__main__':
    calculator_no_exit = Calculator()

    calculator_no_exit.run()
