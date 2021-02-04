from kheiron.stack import Stack
class Calculator:
    def __init__(self):
        """
        Initialise the instance with stack instance
        """
        self.stack = Stack()
        self.expression_list = []
        self.supported_operations = ['+', '-', '*', '/']

    def prefix_calculator(self, expression):
        """
        :param expression: Actual arithmetic expression
        :return: result after evaluating expression
        """
        operands = []
        operation = ""
        result = 0
        for value in expression.split(' '):
            self.stack.push(value)
        if self.stack.size() == 1: #Only one value in stack
            return eval(self.stack.pop())

        while self.stack.size() > 0:
            operand_operator = self.stack.pop()
            if operand_operator not in self.supported_operations:
                operands.append(operand_operator)
            else:
                operation = operand_operator.join([operands.pop(),operands.pop()])
                result = eval(operation)
                self.stack.push(str(result))
        return result

    def infix_calculator(self,expression):
        """
        Function to evaluate the arithmetic expression as infix
        :param expression: Arithmetic expression in infix format
        Eg: ( ( ( 1 + 1 ) / 10 ) - ( 1 * 2 ) )
        :return:
        """
        for value in expression.split(' '):
            if value == ')':
                arithmetic_expression = ""
                # print(self.stack)
                arithmetic_expression = arithmetic_expression + self.expression_list.pop(-3) + \
                                        self.expression_list.pop(-2) + \
                                        self.expression_list.pop(-1)
                # print(arithmetic_expression)
                self.expression_list.append(str(eval(arithmetic_expression)))
            elif value != '(':
                self.expression_list.append(value)

        return eval(self.expression_list.pop())






