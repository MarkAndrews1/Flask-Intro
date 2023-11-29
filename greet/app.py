from flask import Flask
app = Flask(__name__)

@app.route('/welcome')
def welcome_user():
    """Welcomes user"""

    return """<h1>Welcome!</h1>"""

@app.route('/welcome/home')
def welcome_home():
    """Welcomes user home"""

    return """<h1>Welcome Home!</h1>"""

@app.route('/welcome/back')
def welcome_back():
    """Welcomes user back"""
    
    return """<h1>Welcome Back!</h1>"""