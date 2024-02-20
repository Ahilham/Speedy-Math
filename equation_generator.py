import random

class EquationGenerator:
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
        operator = random.choice(operation)

        equation = f"{a} {operator} {b} = ___"
        answer = EquationGenerator.logic[operator](a, b)

        return round(answer, 2), equation

if __name__ == "__main__":

    ans, question = EquationGenerator.equation_gen(2)

    print(question)
    print(ans)

# find a way for level 2 fo division, make it easier as in whole number answer only
