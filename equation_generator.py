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
            
        else:
            range = [10, 100]
        

        a = random.randint(range[0],range[1])
        b = random.randint(range[0],range[1])
        operator = random.choice(operation)

        #making sure division problems are whole number
        if operator == '/':
            divi = (a / b) % 2
            while divi != 0:
                a = random.randint(range[0],range[1])
                b = random.randint(range[0],range[1])
                divi = (a / b) % 2

        answer = EquationGenerator.logic[operator](a, b)

        if level == 1 or level == 2:

            unknown_rand = random.choice(Linear)

            if unknown_rand == 1:
                equation = f"Y {operator} {b} = {int(answer)}"
                unk = a
            else:
                equation = f"{a} {operator} Y = {int(answer)}"
                unk = b
        else:
            c = random.randint(range[0],range[1])
            operator2 = random.choice(operation)
            answer2 = EquationGenerator.logic[operator2](answer, c)

            

            Linear.append(3)

            unknown_rand = random.choice(Linear)

            if unknown_rand == 1:
                equation = f"Y {operator} {b} {operator2} {c} = {int(answer2)}"
                unk = a
            elif unknown_rand == 2:
                equation = f"{a} {operator} Y {operator2} {c} = {int(answer2)}"
                unk = b
            else:
                equation = f"{a} {operator} {b} {operator2} Y = {int(answer2)}"
                unk = c




        

        

        return int(unk), equation

if __name__ == "__main__":

    ans, question = EquationGenerator.equation_gen(3)

    print(question)
    print(ans)

# find a way for level 2 fo division, make it easier as in whole number answer only
