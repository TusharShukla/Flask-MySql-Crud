from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_mysqldb import MySQL



app = Flask(__name__)
app.secret_key = 'many random bytes'

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'fusion90'
app.config['MYSQL_DB'] = 'crud'

mysql = MySQL(app)



@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM students")
    data = cur.fetchall()
    cur.close()
    return render_template('index2.html', students = data )



@app.route('/insert', methods = ['POST'])
def insert():

    if request.method == "POST":
        flash("Data Inserted Successfully")
        name = request.form['name']
        email = request.form['email']
        percentage = request.form['percentage']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO students (name, email, percentage) VALUES (%s, %s, %s)", (name, email, percentage))
        mysql.connection.commit()
        return redirect(url_for('Index'))




@app.route('/delete/<string:id_data>', methods = ['GET'])
def delete(id_data):
    flash("Record Has Been Deleted Successfully")
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM students WHERE id=%s", (id_data,))
    mysql.connection.commit()
    return redirect(url_for('Index'))





@app.route('/update',methods=['POST','GET'])
def update():

    if request.method == 'POST':
        id_data = request.form['id']
        name = request.form['name']
        email = request.form['email']
        percentage = request.form['percentage']
        cur = mysql.connection.cursor()
        cur.execute("""
               UPDATE students
               SET name=%s, email=%s, percentage=%s
               WHERE id=%s
            """, (name, email, percentage, id_data))
        flash("Data Updated Successfully")
        mysql.connection.commit()
        return redirect(url_for('Index'))


@app.route('/get_barchart_data')
def get_barchart_data():
    cur = mysql.connection.cursor()

    #Create
    #cur.execute('''CREATE TABLE data (id INTEGER, name VARCHAR(20), number INTEGER)''')
    
    #Insert values
    #cur.execute('''INSERT INTO data VALUES (1, 'A', 80)''')
    #cur.execute('''INSERT INTO data VALUES (2, 'B', 100)''')
    #cur.execute('''INSERT INTO data VALUES (3, 'C', 56)''')
    #cur.execute('''INSERT INTO data VALUES (4, 'D', 120)''')
    #cur.execute('''INSERT INTO data VALUES (5, 'E', 180)''')
    #cur.execute('''INSERT INTO data VALUES (6, 'F', 30)''')
    #cur.execute('''INSERT INTO data VALUES (7, 'G', 40)''')
    #cur.execute('''INSERT INTO data VALUES (8, 'H', 120)''')
    #cur.execute('''INSERT INTO data VALUES (9, 'I', 160)''')
    #mysql.connection.commit()

    #Read
    cur.execute("""SELECT percentage FROM students""")
    value = cur.fetchall() 
    return jsonify(value) 







if __name__ == "__main__":
    app.run(debug=True)
