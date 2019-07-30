from databases import *
from flask import Flask, render_template, url_for, request
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', students=query_all())

@app.route('/student/<int:student_id>')
def display_student(student_id):
    return render_template('student.html', student=query_by_id(student_id))

#Create an '/add' route here:

@app.route('/add' , methods=['GET' , 'POST'])
def add_student_route():
	if request.method == 'GET' :
		return render_template("add.html")
	else :
		print('Recieved POST request!')
		name=request.form['Student_name']
		year=request.form['Student_year']
		add_student(name , year)
		return render_template("add.html")

@app.route('/delete/<int:student_id>' , methods=['POST'])
def student_id(student_id):
	delete_student_id(student_id)
	return render_template("home.html")


if __name__ == '__main__':
    app.run(debug=True)
