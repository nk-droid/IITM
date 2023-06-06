from flask import Flask, redirect, render_template, request, session, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite3'
db = SQLAlchemy()
db.init_app(app)
app.app_context().push()

class course(db.Model) :
    __tablename__ = 'course'
    course_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    course_code = db.Column(db.String, unique = True, nullable = False)
    course_name = db.Column(db.String, nullable = False)
    course_description = db.Column(db.String)
    enroll = db.relationship("enrollments", backref = 'courses')

class student(db.Model) :
    __tablename__ = 'student'
    student_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    roll_number = db.Column(db.String, unique = True, nullable = False)
    first_name = db.Column(db.String, nullable = False)
    last_name = db.Column(db.String)
    enroll = db.relationship("enrollments", backref = 'students')

class enrollments(db.Model) :
    __tablename__ = 'enrollments'
    enrollment_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    estudent_id = db.Column(db.Integer, db.ForeignKey('student.student_id'), nullable = False)
    ecourse_id = db.Column(db.Integer, db.ForeignKey('course.course_id'), nullable = False)
    stud = db.relationship("student", backref = 'enrollment')

@app.route("/", methods=["GET", "POST"])
def home() :
    students = student.query.all()
    return render_template("index.html", student=students)

@app.route("/student/create", methods=["GET", "POST"])
def add_student() :
    course_dic = {"course_1" : "1",
                "course_2" : "2",
                "course_3" : "3",
                "course_4" : "4"
            }

    if request.method == "GET" :
        return render_template("form.html")
    if request.method == "POST" :
        roll, fname, lname, ecourse = request.form.get('roll'), request.form.get('f_name'), request.form.get('l_name'), request.form.getlist("courses")
        student_record = student(roll_number = roll, first_name = fname, last_name = lname)
        
        try :
            db.session.add(student_record)
            estudent = db.session.query(student.student_id).filter(student.roll_number == student_record.roll_number)
            for course_ele in ecourse :    
                enrollemnt_record = enrollments(estudent_id = estudent, ecourse_id = course_dic[course_ele])
                db.session.add(enrollemnt_record)
                db.session.commit()
            return redirect(url_for('home'))
        except :
            return render_template('studentexists.html')
        
@app.route("/student/<int:student_id>/update", methods=["GET", "POST"])
def update_student(student_id) : 
    course_dic = {"course_1" : "1",
                "course_2" : "2",
                "course_3" : "3",
                "course_4" : "4"
            }
    if request.method == "GET" :
        current_details = student.query.filter(student.student_id == student_id).first()
        current_courses = enrollments.query.with_entities(enrollments.ecourse_id).filter_by(estudent_id = student_id).all()
        current_course = [cour[0] for cour in current_courses]       
        
        return render_template("update_student.html", student = current_details, course = current_course)
    
    if request.method == "POST" :
        stu = student.query.filter(student.student_id == student_id).first()
        (stu.first_name, stu.last_name, ecourse) = (request.form.get("f_name"), request.form.get("l_name"), request.form.getlist('courses'))
        
        enrollments.query.filter(enrollments.estudent_id == student_id).delete()
        for course_ele in ecourse :    
                enrollemnt_record = enrollments(estudent_id = student_id, ecourse_id = course_dic[course_ele])
                db.session.add(enrollemnt_record)        
        db.session.commit()
        return redirect(url_for('home'))

@app.route("/student/<int:student_id>", methods=["GET", "POST"])
def specific_student(student_id) :    
     
    students = student.query.filter(student.student_id == student_id).first()

    current_courses = enrollments.query.with_entities(enrollments.ecourse_id).filter_by(estudent_id = student_id).all()
    current_course = [cour[0] for cour in current_courses]
    enrollment_table = course.query.filter(course.course_id.in_(current_course))
    
    return render_template("specific_student.html", student=students, enrollment_table=enrollment_table)

@app.route("/student/<int:student_id>/delete", methods=["GET", "POST"])
def delete_student(student_id) :
    student.query.filter(student.student_id == student_id).delete()
    enrollments.query.filter(enrollments.estudent_id == student_id).delete()
    db.session.commit()
    return redirect(url_for('home'))

if __name__ == "__main__" :
    app.run(debug=True)