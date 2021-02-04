from kheiron.calculator import Calculator
from kheiron_rest_server import app

REST_PORT = 8085
def get_user_input():
    """
        Read user input for arithmetic expressions
    :return:
    """
    print("*******Kheiron Calculator (Prefix/Infix)*********\n \nType q to exit\n")
    calculator = Calculator()
    while True:
        expression = input(">")
        if expression.find('(') != -1: #seems like infix expression
            print(calculator.infix_calculator(expression))
        elif expression == 'q':
            exit(0)
        else:
            print(calculator.prefix_calculator(expression))

def start_rest_server():
    """
    Function to start the rest server
    :return: None
    """
    app.run(host='0.0.0.0', port=REST_PORT, debug=False)

if __name__ == '__main__':
    start_mode = int(input("Which mode you want to start the application (1.Console/2.Rest Server) >"))
    if start_mode == 1:
        get_user_input()
    elif start_mode == 2:
        start_rest_server()
    else:
        raise Exception("Invalid start mode")
