import re

def arithmetic_arranger(problems, show_answers=False):


    if len(problems) > 5:
        return "Error: Too many problems."


    numbers = [[num for num in re.findall(r'\d+', expr)] for expr in problems]
    operators = [re.sub(r'\d+', '', expr).strip() for expr in problems]


    if any(not num.isdigit() for expr in problems for num in re.findall(r'\S+', expr) if num not in operators):
        return "Error: Numbers must only contain digits."


    if any(op not in ['+', '-'] for op in operators):
        return "Error: Operator must be '+' or '-'."


    numbers = [[int(num) for num in num_list] for num_list in numbers]
    if any(k > 9999 or g > 9999 for k, g in numbers):
        return "Error: Numbers cannot be more than four digits."


    spacesup = [max(len(str(a)), len(str(b))) for a, b in numbers]


    first_line, second_line, separator_line, answer_line = [], [], [], []

    for i in range(len(problems)):
        width = spacesup[i] + 2  # Space for operator
        first_line.append(str(numbers[i][0]).rjust(width))
        second_line.append(operators[i] + " " + str(numbers[i][1]).rjust(spacesup[i]))
        separator_line.append("-" * width)

        if show_answers:
            result = numbers[i][0] + numbers[i][1] if operators[i] == "+" else numbers[i][0] - numbers[i][1]
            answer_line.append(str(result).rjust(width))


    arranged_problems = "\n".join([
        "    ".join(first_line),
        "    ".join(second_line),
        "    ".join(separator_line)
    ])

    if show_answers:
        arranged_problems += "\n" + "    ".join(answer_line)

    return arranged_problems


print(arithmetic_arranger(["98 + 35", "3801 - 2", "45 + 43", "123 + 49"], show_answers=True))
