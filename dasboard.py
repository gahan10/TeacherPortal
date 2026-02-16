from flask import Blueprint, render_template, request, redirect, url_for
from __init__ import db
import students
from flask_login import login_required
# from run import app

studentbp = Blueprint("student", __name__)

# View all students
@studentbp.route("/dashboard", methods=["GET"])
@login_required
def fetch():
    students_list = students.Students.query.all()
    return render_template("dashboard.html", students=students_list)

@studentbp.route("/add", methods=["POST"])
def add():
    name = request.form.get("name")
    subject = request.form.get("subject")
    marks = request.form.get("marks")
    new_student = students.Students(name=name, subject=subject, marks=marks)
    db.session.add(new_student)
    db.session.commit()
    student_list = students.Students.query.all()
    return render_template("dashboard.html", students=student_list)

@studentbp.route("/update/<int:id>", methods=["POST"])
def update(id, name=None, subject=None, marks=None):
    print("id", id)
    student =  students.Students.query.filter_by(id=id).first()
    print(request.form.get("name"), request.form.get("subject"), request.form.get("marks"))
    if student:
        if request.form.get("name"):
            student.name = request.form.get("name")
        if request.form.get("subject"):
            student.subject =  request.form.get("subject")
        if request.form.get("marks"):
            student.marks = request.form.get("marks")
        db.session.commit()
        students_list = students.Students.query.all()
        return render_template("dashboard.html", students=students_list)
 
    return False

@studentbp.route("/delete/<int:id>", methods=["POST"])
def delete(id):
    student = students.Students.query.filter_by(id=id).first()
    if student:
        db.session.delete(student)
        db.session.commit()
        students_list = students.Students.query.all()
        return render_template("dashboard.html", students=students_list)
    return False
