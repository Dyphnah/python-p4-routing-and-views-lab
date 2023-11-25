#!/usr/bin/env python3

from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    return '<h1>Python Operations with Flask Routing and Views</h1>'

@app.route('/print/<parameter>')
def print_route(parameter):
    return parameter

@app.route('/print/<string:param>')
def print_text(param):
    print("hello")
    return f'Printed String: {param}'

@app.route('/count/int:param')
def count(param):
    numbers = '\n'.join(str(i) for i in range(param + 1))
    return f'<h1>Numbers:</h1><pre>{numbers}</pre>'

@app.route('/math/<param>')
def math(param):
    num1 = float(param.split()[0])
    operation = param.split()[1]
    num2 = float(param.split()[2])

    result = None

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == '*':
        result = num1 * num2
    elif operation == 'div':
        if num2 != 0:
            result = num1 / num2
        else:
            return '<h1>Error: Division by zero</h1>'
    elif operation == '%':
        result = num1 % num2
    else:
        return '<h1>Error: Invalid operation</h1>'

    return f'<h1>Result of {num1} {operation} {num2}: {result}</h1>'


if __name__ == '__main__':
    app.run(port=5555, debug=True)
