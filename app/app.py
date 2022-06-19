from flask import Flask, redirect, url_for, request
app = Flask(__name__)

@app.route('/')
def default():
    return 'Welcome to the website'
@app.route('/hello')
def hello():
    return 'Hello World'
@app.route('/success/<name>')
def success(name):
    return 'Welcome %s' % name

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        user = request.form['nm']
        return redirect(url_for('success',name = user))
    else:
        user = request.args.get('nm')
        return redirect(url_for('success',name = user))

if __name__ == '__main__':
    app.run(debug = True, host="0.0.0.0")