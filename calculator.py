def get_number(prompt):
    while True:
        try:
            num = float(input(prompt))
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
        boolli = input(prompt).strip()
        if boolli in ("Y", "y", "YES", "Yes", "yes"):
            return True
        if boolli in ("N", "n", "NO", "No", "no"):
            return False
        else:
            print("Invalid response. Please enter [Y|N].")


class Calculator:
    def __init__(self, num1_prompt, operator_prompt,
                 num2_prompt, goodbye_msg=None):
        self.__num1prompt = num1_prompt
        self.__operator_prompt = operator_prompt
        self.__num2prompt = num2_prompt
        self.__goodbye_msg = goodbye_msg

    def calculate(self):
        x = get_number(self.__num1prompt)
        opp = get_operator(self.__operator_prompt)
        y = get_number(self.__num2prompt)
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
        if z is not None:
            print(f"{x} {opp} {y} = {z}")
        return z

    def run(self):
        answers = []
        while True:
            result = self.calculate()
            if result is not None:
                answers.append(result)
            if not halt("Would you like to continue? [Y|N]: "):
                break
        if len(answers) > 1:
            c = "calculations"
        else:
            c = "calculation"
        print(f"You carried out {len(answers)} {c}. The results were {'; '.join(map(str, answers))}")
        if self.__goodbye_msg is not None:
            print(self.__goodbye_msg)


if __name__ == '__main__':
    calculator_no_exit = Calculator("Enter the first number: ", "Enter the operator: ",
                                    "Enter the second number: ", "Bye!")

    calculator_no_exit.run()
