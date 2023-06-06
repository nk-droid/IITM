from flask import Flask, request, render_template
from matplotlib import pyplot as plt
import statistics as st

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])


def index() :
    fi = open('data.csv', 'r')
    data, students_id, course_id = [], [], []
    lines = fi.readlines()

    for line in lines :
        lin = list(map(lambda x: x.strip(" "),list(line.split(","))))
        data += [lin]
        students_id.append(lin[0])
        course_id.append(lin[1])

    if request.method == "GET" :
        return render_template("index.html")
    if request.method == "POST" :
        if request.form.get("ID") == "student_id" :
            imp_data, total, inp = [], [], request.form.get("value")
            if  inp in students_id :
                for j in range(len(data)) :
                    if data[j][0] == inp :
                        imp_data.append(data[j])
                        total.append(int(data[j][2]))
                total_mrks = sum(total)        

                return render_template("student.html", imp_data=imp_data, total_mrks=total_mrks)
            else :
                return render_template("other.html")


        if request.form.get("ID") == "course_id" :
            target_marks, inp = [], request.form.get("value")
            if inp in course_id :
                for i in range(len(data)) :
                    if data[i][1] == inp :
                        target_marks.append(int(data[i][2]))
                avg_marks, max_marks = st.mean(target_marks), max(target_marks)

                plt.hist(target_marks)
                plt.xlabel("Marks")
                plt.ylabel("Frequency")
                plt.legend()
                plt.savefig("static/graph.png")
                
                return render_template("course.html", avg_marks=avg_marks, max_marks=max_marks)
            else :
                return render_template("other.html")

                
if __name__ == "__main__" :
    app.run()