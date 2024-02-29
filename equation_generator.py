import random
import operator


class EquationGenerator:
    logic = {
   
        '+' : operator.add,
        '-' : operator.sub,
        '/' : operator.truediv,
        'x' : operator.mul
    }

    @staticmethod
    def equation_gen( level: int):
        range = []
        Linear = [1, 2]
        range = [1, 10]

        if level == 1:
            operation = ['+', '-']
            
        else:
            operation = ['+', '-', '/', 'x']
        

        a = random.randint(range[0],range[1])
        b = random.randint(range[0],range[1])
        operator = random.choice(operation)

        #making sure division problems are whole number
        

        answer = EquationGenerator.logic[operator](a, b)

        if level == 1 or level == 2:

            if operator == '/':
                divi = (a / b) % 2
                while divi != 0:
                    a = random.randint(range[0],range[1])
                    b = random.randint(range[0],range[1])
                    divi = (a / b) % 2

            unknown_rand = random.choice(Linear)

            if unknown_rand == 1:
                equation = f"Y {operator} {b} = {int(answer)}"
                unk = a
            else:
                equation = f"{a} {operator} Y = {int(answer)}"
                unk = b
        else:
            answer2 = 3
            while answer2 % 2 != 0:
                a = random.randint(range[0],range[1])
                b = random.randint(range[0],range[1])
                c = random.randint(range[0],range[1])
                operator = random.choice(operation)
                operator2 = random.choice(operation)
                
                if (operator2 == "/" or operator2 == "x") and (operator != "/" or operator != "x"):
                    

                    if operator2 == '/':
                        divi = (b / c) % 2
                        while divi != 0:
                            b = random.randint(range[0],range[1])
                            c = random.randint(range[0],range[1])
                            divi = (b / c) % 2

                    answer = EquationGenerator.logic[operator2](b, c)
                    answer2 = EquationGenerator.logic[operator](a, answer)
                else:
                    if operator == '/':
                        divi = (b / c) % 2
                        while divi != 0:
                            b = random.randint(range[0],range[1])
                            c = random.randint(range[0],range[1])
                            divi = (b / c) % 2
                    
                    answer = EquationGenerator.logic[operator](a, b)
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
    
# if __name__ == "__main__":
#     ans, equation,a ,b ,c = EquationGenerator.equation_gen(3)
#     print(f"{equation} {a} {b} {c}")
#     print(ans)

