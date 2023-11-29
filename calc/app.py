from flask import Flask, request
from operations import add, sub, mult, div
app = Flask(__name__)

operations = {
    'add': add, 
    'sub': sub, 
    'mult': mult, 
    'div': div 
}

@app.route('/add')
def addition():
    """adds a and b"""

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    total = str(add(a, b))
    return total

@app.route('/sub')
def subtraction():
    """subtracts a and b"""

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    total = str(sub(a, b))
    return total

@app.route('/mult')
def multiplication():
    """multiplies a and b"""

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    total = str(mult(a, b))
    return total

@app.route('/div')
def division():
    """divides a and b"""

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    total = str(div(a, b))
    return total

@app.route('/math/<op>')
def math(op):
    """does math depending on operator"""

    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    total = str(operations[op](a, b))
    return total