def arithmetic_arranger(problems, run=False):
    # Initialize Variables
    arranged_problems = ''
    n1 = []
    op = []
    n2 = []
    ans = []
    # Test for if number of problems exceeds 4 InputError()
    if len(problems) >= 6:
        return 'Error: Too many problems.'

    # Breaks up problem into number 1, operator, and number 2
    for problem in problems:
        n1.append(problem.split(' ')[0])
        op.append(problem.split(' ')[1])
        n2.append(problem.split(' ')[2])

    for i in range(len(problems)):
        # Test for if other operator is used DigitError()
        if not n1[i].isdigit():
            return "Error: Numbers must only contain digits."
        # Test for if len number is 4 digits LargeError()
        if len(n1[i]) >= 5:
            return "Error: Numbers cannot be more than four digits."
        length = max(len(n1[i]), len(n2[i])) + 2

        arranged_problems += n1[i].rjust(length) + '    '
    arranged_problems = arranged_problems.rstrip() + '\n'

    for i in range(len(problems)):
        # Test for if other operator is used OperatorError()
        if op[i] != '+':
            if op[i] != '-':
                return "Error: Operator must be '+' or '-'."

        # Test for if other operator is used DigitError()
        if not n2[i].isdigit():
            return "Error: Numbers must only contain digits."
        # Test for if len number is 4 digits LargeError()
        if len(n2[i]) >= 5:
            return "Error: Numbers cannot be more than four digits."
        # find max length for problem
        length = max(len(n1[i]), len(n2[i])) + 2

        arranged_problems += op[i] + n2[i].rjust(length - 1) + '    '
    arranged_problems = arranged_problems.rstrip() + '\n'

    for i in range(len(problems)):
        length = max(len(n1[i]), len(n2[i])) + 2
        for j in range(length):
            arranged_problems += '-'
        arranged_problems += '    '

    if run:
        arranged_problems = arranged_problems.rstrip() + '\n'
        for i in range(len(problems)):
            if op[i] == '+':
                ans.append(str(int(n1[i]) + int(n2[i])))
            elif op[i] == '-':
                ans.append(str(int(n1[i]) - int(n2[i])))
            length = max(len(n1[i]), len(n2[i])) + 2
            arranged_problems += ans[i].rjust(length) + '    '
        arranged_problems = arranged_problems.rstrip()
        return arranged_problems
    else:
        arranged_problems = arranged_problems.rstrip()
        return arranged_problems
