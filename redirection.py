from flask import *

app = Flask(__name__)

@app.route('/admin')
def admin():
    return 'admin'

@app.route('/teacher')
def teacher():
    return 'teacher'

@app.route('/student')
def student():
    return 'student'

@app.route('/user/<name>')
def user(name):
    if name == 'admin':
        return redirect(url_for('admin'))
    
    if name == 'teacher':
        return redirect(url_for('teacher'))
    
    if name == 'student':
        return redirect(url_for('student'))

if __name__ =='__main__':
    app.run(debug = True)
