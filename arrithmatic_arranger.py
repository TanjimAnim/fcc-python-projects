def check_operators(element):
    expression = element[1]
    if (expression != "+" and expression != "-"):
        raise Exception("Error: Operator must be '+' or '-'.")


def check_digit(element):
    if not (element[0].isdigit() or element[2].isdigit()):
        raise Exception("Error: Numbers must only contain digits.")
    if (len(element[0]) > 4 or len(element[2]) > 4):
        raise Exception("Numbers cannot be more than four digits.")


def arithmetic_arranger(problems, show_result=False):
    arranged_arr = []
    if (len(problems) > 5):
        raise Exception("Error: Too many problems.")

    for problem in problems:
        check_operators(problem.split())
        check_digit(problem.split())
        arranged_arr.append(arrange(problem.split(), show_result))
    print(arranged_arr)


def arrange(element, show_result=False):
    first_elem = element[0]
    expression = element[1]
    second_elem = element[2]
    if (len(first_elem) > len(second_elem)):
        number_of_dashes = len(first_elem)
    else:
        number_of_dashes = len(second_elem)
    if show_result:
        result = eval(' '.join(element))
    else:
        result = ""
    width = number_of_dashes + 2
    whitespace_without_operator = " " * (width - len(first_elem))
    first_line = f"{whitespace_without_operator}{first_elem}"
    whitespace_with_operator = " " * \
        (len(first_line) - len(f"{expression}{second_elem}"))
    second_line = f"{expression}{whitespace_with_operator}{second_elem}"
    third_line = f"{whitespace_without_operator}{result}"
    arrangement = f"{first_line}\n{second_line}\n{'-' * width}\n{third_line}"
    # print(arrangement)
    #   arrangement = f'{first_elem:>{width - len(first_elem) + 1}}\n{expression} {second_elem.rjust(width - len(second_elem))}\n{"-" * width}\n{str(result):>{width - len(first_elem) + 1}}'
    return arrangement


arithmetic_arranger(
    ["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49", "523 + 49"], True)
