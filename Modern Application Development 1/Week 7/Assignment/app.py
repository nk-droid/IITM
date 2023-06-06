from flask import Flask, redirect, request, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///week7_database.sqlite3'
db = SQLAlchemy()
db.init_app(app)
app.app_context().push()

class Student(db.Model) :
    __tablename__ = 'student'
    student_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    roll_number = db.Column(db.String, unique = True, nullable = False)
    first_name = db.Column(db.String, nullable = False)
    last_name = db.Column(db.String)
    enroll = db.relationship("Enrollments", backref = 'student')

class Course(db.Model) :
    __tablename__ = 'course'
    course_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    course_code = db.Column(db.String, unique = True, nullable = False)
    course_name = db.Column(db.String, nullable = False)
    course_description = db.Column(db.String)
    enroll = db.relationship("Enrollments", backref = 'course')

class Enrollments(db.Model) :
    __tablename__ = 'enrollments'
    enrollment_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    estudent_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), nullable = False)
    ecourse_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), nullable = False)
    stu = db.relationship("Student", backref = 'enrollment')
    cour = db.relationship("Course", backref = 'enrollment')

@app.route("/", methods = ["GET"])
def home() :
    students = Student.query.all()
    return render_template("index.html", students = students)

@app.route("/student/create", methods = ["GET", "POST"])
def add_student() :
    if request.method == "GET" :
        return render_template("add_student.html")
    if request.method == "POST" :
        fname, lname, roll = request.form.get("f_name"), request.form.get("l_name"), request.form.get("roll")
        student = Student(first_name = fname, last_name = lname, roll_number = roll)
        try :
            db.session.add(student)
            db.session.commit()
            return redirect(url_for("home"))
        except :
            return render_template("student_exists.html")

@app.route("/student/<int:student_id>/update", methods = ["GET", "POST"])
def update_student(student_id) :
    if request.method == "GET" :
        student = Student.query.filter(Student.student_id == student_id).first()
        courses = Course.query.all()
        return render_template("update_student.html", student = student, courses = courses)
    if request.method == "POST" :
        student = Student.query.filter(Student.student_id == student_id).first()
        cid = [course.course_id for course in Course.query.all()]
        student.first_name, student.last_name = request.form.get("f_name"), request.form.get("l_name")
        new_enrollment = Enrollments(estudent_id = student_id, ecourse_id = request.form.get("course"))
        enrollments = Enrollments.query.with_entities(Enrollments.ecourse_id, Enrollments.estudent_id).all()
        if (int(new_enrollment.ecourse_id), new_enrollment.estudent_id) not in enrollments :
            db.session.add(new_enrollment)
            db.session.commit()
        return redirect(url_for("home"))
        
@app.route('/student/<int:student_id>/delete', methods = ["GET"])
def delete_student(student_id) :
    Student.query.filter(Student.student_id == student_id).delete()
    Enrollments.query.filter(Enrollments.estudent_id == student_id).delete()
    db.session.commit()
    return redirect(url_for("home"))

@app.route('/student/<int:student_id>', methods = ["GET"])
def student_details(student_id) :
    student = Student.query.filter(Student.student_id == student_id).first()
    current_courses = Enrollments.query.with_entities(Enrollments.ecourse_id).filter_by(estudent_id = student_id).all()
    current_course = [cour[0] for cour in current_courses]
    enrollment_table = Course.query.filter(Course.course_id.in_(current_course))
    return render_template("specific_student.html", student = student, enrollment_table = enrollment_table)

@app.route('/student/<int:student_id>/withdraw/<int:course_id>', methods = ["GET"])
def withdraw_course(student_id, course_id) :
    Enrollments.query.filter(Enrollments.estudent_id == student_id, Enrollments.ecourse_id == course_id).delete()
    db.session.commit()
    return redirect(url_for("home"))

@app.route('/courses', methods = ["GET"])
def course_home() :
    courses = Course.query.all()
    return render_template("course.html", courses = courses)
    
@app.route('/course/create', methods = ["GET", "POST"])
def add_course() :
    if request.method == "GET" :
        return render_template("add_course.html")
    if request.method == "POST" :
        code, c_name, c_desc = request.form.get("code"), request.form.get("c_name"), request.form.get("desc")
        course = Course(course_code = code, course_name = c_name, course_description = c_desc)
        try :    
            db.session.add(course)
            db.session.commit()
            return redirect(url_for("course_home"))
        except :
            return render_template("course_exists.html")

@app.route('/course/<int:course_id>/update', methods = ["GET", "POST"])
def update_course(course_id) :
    if request.method == "GET" :
        course = Course.query.filter(Course.course_id == course_id).first()
        return render_template("update_course.html", course = course)
    if request.method == "POST":
        course = Course.query.filter(Course.course_id == course_id).first()
        course.course_name = request.form.get("c_name")
        course.course_description = request.form.get("desc")
        db.session.commit()
        return redirect(url_for("course_home"))

@app.route('/course/<int:course_id>/delete', methods = ["GET"])
def delete_course(course_id) :
    Course.query.filter(Course.course_id == course_id).delete()
    Enrollments.query.filter(Enrollments.ecourse_id == course_id).delete()
    db.session.commit()
    return redirect(url_for("home"))

@app.route('/course/<int:course_id>', methods = ["GET"])
def course_detail(course_id) :
    course = Course.query.filter(Course.course_id == course_id).first()
    current_students = Enrollments.query.with_entities(Enrollments.estudent_id).filter_by(ecourse_id = course_id).all()
    current_student = [stu[0] for stu in current_students]
    enrollment_table = Student.query.filter(Student.student_id.in_(current_student))
    return render_template("specific_course.html", course = course, enrollment_table = enrollment_table)

if __name__ == "__main__" :
    app.run()