import random

class EquationGenerator:
    numbers = []
    logic = {
   
        '+' : lambda x, y: x + y,
        '-' : lambda x, y: x - y,
        '/' : lambda x, y: x / y,
        'x' : lambda x, y: x * y
    }

    @staticmethod
    def equation_gen( level: int):
        range = []
        operation = []

        if level == 1:
            range = [0, 10]
            operation = ['+', '-']
        elif level == 2:
            range = [10, 100]
            operation = ['+', '-', '/', 'x']

        a = random.randint(range[0],range[1])
        b = random.randint(range[0],range[1])

        equation = EquationGenerator.logic[random.choice(operation)](a, b)

        return equation


print(EquationGenerator.equation_gen(1))


