import random
import itertools

# define a list of numbers
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# randomly select 4 numbers from the list, with the possibility of selecting the same number multiple times
selected_numbers = random.choices(numbers, k=4)

# print the selected numbers
print("Selected numbers:", selected_numbers)


# loop through all possible orders of the four numbers

no_solution = True
for order in itertools.permutations(selected_numbers):
    # try all possible combinations of mathematical operations
    for op1 in ['+', '-', '*', '/']:
        for op2 in ['+', '-', '*', '/']:
            for op3 in ['+', '-', '*', '/']:
                # try to evaluate the expression
                expr = f"({order[0]} {op1} {order[1]}) {op2} ({order[2]} {op3} {order[3]})"
                try:
                    result = eval(expr)
                    # if the result is 24, print the expression
                    if result == 24 or result==24.0:
                        print("Found solution:", expr)
                        no_solution = False

                except ZeroDivisionError:
                    pass


# e.g. [1,5,5,5], (5-1/5)*5
for order in itertools.permutations(selected_numbers):
    # try all possible combinations of mathematical operations
    for op1 in ['+', '-', '*', '/']:
        for op2 in ['+', '-', '*', '/']:
            for op3 in ['+', '-', '*', '/']:
                # try to evaluate the expression
                expr = f"({order[0]} {op1} {order[1]} {op2} {order[2]}) {op3} {order[3]}"
                try:
                    result = eval(expr)
                    # if the result is 24, print the expression
                    if result == 24 or result==24.0:
                        print("Found solution:", expr)
                        no_solution = False

                except ZeroDivisionError:
                    pass

# e.g. [2,4,11,12], (11-2)*4-12
for order in itertools.permutations(selected_numbers):
    # try all possible combinations of mathematical operations
    for op1 in ['+', '-', '*', '/']:
        for op2 in ['+', '-', '*', '/']:
            for op3 in ['+', '-', '*', '/']:
                # try to evaluate the expression
                expr = f"({order[0]} {op1} {order[1]}) {op2} {order[2]} {op3} {order[3]}"
                try:
                    result = eval(expr)
                    # if the result is 24, print the expression
                    if result == 24 or result==24.0:
                        print("Found solution:", expr)
                        no_solution = False

                except ZeroDivisionError:
                    pass

# e.g. [3,3,8,8], 8/(3-8/3), [1,4,5,6], 4/(1-5/6)
# are these two the only cases where a op (b op c op d) format is used? also the result will not be an integer

for order in itertools.permutations(selected_numbers):
    # try all possible combinations of mathematical operations
    # only examine the a / (b op c op d) format
    op1 = '/'
    for op2 in ['+', '-', '*', '/']:
        for op3 in ['+', '-', '*', '/']:
            # try to evaluate the expression
            expr = f"{order[0]} {op1} ({order[1]} {op2} {order[2]} {op3} {order[3]})"
            try:
                result = eval(expr)
                # if the result is 24, print the expression
                if abs(result-24)<0.0001:
                    print("Found solution:", expr)
                    no_solution = False

            except ZeroDivisionError:
                pass

# if no solution was found, print a message
if no_solution:
    print("No solution found.")


# interesting examples 3,3,7,7; 1,5,5,5; 

# print(8/(3-8/3))
# print(4/(1-5/6))
