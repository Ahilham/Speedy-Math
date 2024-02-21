import random
import math

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
        operation = ['+', '-', '/', 'x']
        Linear = [1, 2]

        if level == 1:
            range = [1, 10]
            
        elif level == 2:
            range = [10, 100]
        

        a = random.randint(range[0],range[1])
        b = random.randint(range[0],range[1])
        operator = random.choice(operation)

        if operator == '/':
            divi = (a / b) % 2
            while divi != 0:
                a = random.randint(range[0],range[1])
                b = random.randint(range[0],range[1])
                divi = (a / b) % 2

        answer = EquationGenerator.logic[operator](a, b)

        unknown_rand = random.choice(Linear)

        if unknown_rand == 1:
            equation = f"Y {operator} {b} = {int(answer)}"
            unk = a
        else:
            equation = f"{a} {operator} Y = {int(answer)}"
            unk = b

        

        return int(unk), equation

if __name__ == "__main__":

    ans, question = EquationGenerator.equation_gen(2)

    print(question)
    print(ans)

# find a way for level 2 fo division, make it easier as in whole number answer only
