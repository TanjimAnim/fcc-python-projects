def check_operators(element):
    expression = element[1]
    if expression not in ['+', "-"]:

        return "Error: Operator must be '+' or '-'."


def check_digit(element):
    if not (element[0].isdigit() and element[2].isdigit()):
        return "Error: Numbers must only contain digits."
    if (len(element[0]) > 4 or len(element[2]) > 4):
        return "Error: Numbers cannot be more than four digits."


def arithmetic_arranger(problems, show_result=False):
    arranged_arr = []
    error_messages = []
    if (len(problems) > 5):
        return "Error: Too many problems."

    for problem in problems:
        operator_error = check_operators(problem.split())
        digit_error = check_digit(problem.split())

        if operator_error:
            error_messages.append(operator_error)
        elif digit_error:
            error_messages.append(digit_error)
        else:
            arranged_arr.append(arrange(problem.split(), show_result))
    formatted_lines = []

    for line_group in zip(*arranged_arr):
        joined_group = "    ".join(line_group)
        formatted_lines.append(joined_group)

    final_formatted_output = "\n".join(formatted_lines)
    return final_formatted_output


def arrange(element, show_result=False):
    first_elem = element[0]
    expression = element[1]
    second_elem = element[2]
    if expression not in ['+', "-"]:
        return "Error: Operator must be '+' or '-'."
    number_of_dashes = max(len(first_elem), len(second_elem))
    first_line = ""
    second_line = ""
    dashes_line = ""
    if show_result:
        result = eval(' '.join(element))
    else:
        result = ""
    width = number_of_dashes + 2
    whitespace_without_operator = " " * (width - len(first_elem))
    first_line += f"{whitespace_without_operator}{first_elem}"
    whitespace_with_operator = " " * \
        (len(first_line) - len(f"{expression}{second_elem}"))
    second_line += f"{expression}{whitespace_with_operator}{second_elem}"
    dashes_line += f"{'-' * width}"
    if show_result:
        whitespace_for_result = " " * (width - len(str(result)))
        third_line = f"{whitespace_for_result}{result}"
        return first_line, second_line, dashes_line, third_line
    return first_line, second_line, dashes_line


# print(arithmetic_arranger(['24 + 85215', '3801 - 2', '45 + 43', '123 + 49']))
