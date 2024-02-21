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

        if level == 1:
            range = [0, 10]
            
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



        equation = f"{a} {operator} {b} = ___"
        answer = EquationGenerator.logic[operator](a, b)

        return int(answer), equation

if __name__ == "__main__":

    ans, question = EquationGenerator.equation_gen(1)

    print(question)
    print(ans)

# find a way for level 2 fo division, make it easier as in whole number answer only
