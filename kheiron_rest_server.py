from flask import Flask
from flask import request,jsonify
from kheiron.calculator import Calculator

app = Flask(__name__)

@app.route('/kheiron/api/v1/calculator', methods=['POST'])
def calculator_handle():
    contents = request.json
    calculator = Calculator()
    if contents.get('expression') != None:
        if '(' in contents['expression']:
            #possibly an infix notation
            result = {}
            result['result']=calculator.infix_calculator(contents['expression'])
            return jsonify(result)
        else: #possibly a prefix
            result = {}
            result['result'] = calculator.prefix_calculator(contents['expression'])
            return jsonify(result)
    else:
        return "Invalid expression", 500
