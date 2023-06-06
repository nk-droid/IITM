from matplotlib import pyplot as plt
import sys
import statistics as st
from jinja2 import Template

inp1, inp2 = sys.argv[1], sys.argv[2]
fi = open('data.csv', 'r')
data, students_id, course_id = [], [], []
lines = fi.readlines()

for line in lines :
    lin = list(map(lambda x: x.strip(" "),list(line.split(","))))
    data += [lin]
    students_id.append(lin[0])
    course_id.append(lin[1])

if inp1 == '-s' and inp2 in students_id :
    imp_data, total = [], []
    for j in range(len(data)) :
        if inp2 == data[j][0] :
            imp_data.append(data[j])
            total.append(int(data[j][2]))

    total_mrks = sum(total)

    content = Template("""
<!DOCTYPE html>
<html>
    <head>
        <title>Student Data</title>
    </head>
    <body>
        <div><h1>Student Details</h1></div>
        <div>
            <table border = "1.5px solid black">
                <tr>
                    <th>Student id</th>
                    <th>Course id</th>
                    <th>Marks</th>
                </tr>
                
                {% for line in imp_data %}
                    <tr>
                        <td>{{ line[0] }}</td>
                        <td>{{ line[1] }}</td>
                        <td>{{ line[2] }}</td>
                    </tr>
                {% endfor %}
                <tr>
                    <td align = " center" colspan = '2'>Total Marks</td>
                    <td> {{ total_mrks }} </td>
                </tr>
            </table>
        </div>

    </body>
</html>
""")

    html = content.render(imp_data=imp_data, total_mrks=total_mrks)

elif inp1 == '-c' and inp2 in course_id :
    #avg marks and max marks calculation for the table
    target_marks = []
    for i in range(len(data)) :
        if data[i][1] == inp2 :
            target_marks.append(int(data[i][2]))
    avg_marks, max_marks = st.mean(target_marks), max(target_marks)

    plt.hist(target_marks)
    plt.xlabel("Marks")
    plt.ylabel("Frequency")
    plt.legend()
    plt.savefig("graph.png")

    #html content generation
   
    content = Template("""
<!DOCTYPE html>
<html>
    <head>
        <title>
            Course Data
        </title>
    </head>
    <body>
        <div>
            <h1>
                Course Details
            </h1>
        </div>
        <div>
            <table border = "1.5px solid black">
                <tr>
                    <th>
                        Average Marks
                    </th>
                    <th>
                        Maximum Marks
                    </th>
                </tr>
                <tr>
                    <td>
                        {{ avg_marks }}
                    </td>
                    <td>
                        {{ max_marks }}
                    </td>
                </tr>
            </table>
        </div>
        <img alt="graph of the marks" src="graph.png"/>
    </body>
</html>
""")

    html = content.render(avg_marks=avg_marks, max_marks=max_marks)
    
else :    
    content = Template("""
<!DOCTYPE html>
<html>
    <head>
        <title>Something went wrong</title>
    </head>
    <body>
        <div>
            <h1>
                Wrong Inputs
            </h1>
        </div>
        <div>
            Something went wrong
        </div>

    </body>
</html>
""")

    html = content.render()


def main() :
    f = open("output.html","w")
    f.write(html)
    f.close()

if __name__ == "__main__" :
    main()