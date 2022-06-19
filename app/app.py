"""
high level support for doing this and that.
"""
from flask import Flask, redirect, url_for, request
app = Flask(__name__)


@app.route('/')
def default():
    """
high level support for doing this and that.
"""
    return 'Welcome to the website'


@app.route('/hello')
def hello():
    """
high level support for doing this and that.
"""
    return 'Hello World'


@app.route('/success/<name>')
def success(name):
    """
high level support for doing this and that.
"""
    return 'Welcome %s' % name


@app.route('/login', methods=['POST', 'GET'])
def login():
    """
high level support for doing this and that.
"""
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success', name=user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success', name=user))


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
