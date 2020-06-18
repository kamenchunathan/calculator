"""determination of order of evaluation of the problem"""

least_precedence = 1
supported_operations = {
    '+': [1, lambda a, b: a + b],
    '-': [1, lambda a, b: a - b],
    '/': [0, lambda a, b: a / b],
    '*': [0, lambda a, b: a * b]
}


def determine_order_of_operation(operands, operations):
    # reduce to simplest possible problem
    solution = None
    num_of_operations = len(operations)
    for precedence in range(least_precedence + 1):
        i = 0
        while i < num_of_operations:
            if len(operations) == 1:
                solution = compute(operations[0][1], operands[0], operands[1])
            elif operations[i][0] == precedence :
                res = compute(operations[i][1], operands[i], operands[i + 1])
                # update related values
                operations.remove(operations[i])
                operands[i:i+2] = [res]
                num_of_operations = len(operations)
            i += 1
    return solution


# deprecated
def calculate_op_of_same_precedence(operands, operations_in_order):
    """takes a list of operands and a list of operations with the same precedence
    and returns the result of the calculations"""
    # perform checks to see number of operators matches the numbers given
    if len(operands) != len(operations_in_order):
        raise Exception('different number of operators and operands')

    result = 0
    for i in range(len(operands)):
        for op in supported_operations.keys():
            if operations_in_order[i] == op:
                result = compute(supported_operations[op][1], result, operands[i])
    return result


def compute(operation, a, b):
    return operation(a, b)

# -------------------------------------------------------tests-------------------------------------------------
def test():
    print(determine_order_of_operation([2,2,3,78],[supported_operations['+']] * 3))


if __name__ == '__main__':
    test()