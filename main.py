from flask import Flask, render_template,request

import mysql.connector
app = Flask(__name__)

mydb = mysql.connector.connect(
    host="localhost",
    user = "root",
    password="",
    database = "restaurant"

)

mycursor = mydb.cursor()

@app.route("/", methods=["POST","GET"])

def index():
    if request.method == "POST":
        Name = request.form.get("Name")
        email = request.form.get("email")
        Date_time = request.form.get("date_time")
        selected = request.form.get("select")
        Special_req =request.form.get("Special_req")
        mycursor.execute('INSERT INTO Table_book (Name, email, Date_time,selected,Special_req) VALUES (%s, %s,%s,%s,%s)', (Name, email, Date_time,selected,Special_req))
        mydb.commit()
    return render_template("index.html")


@app.route("/book",methods=["POST","GET"])
def book():
    if request.method == "POST":
        Name = request.form.get("Name")
        email = request.form.get("email")
        Date_time = request.form.get("date_time")
        selected = request.form.get("select")
        Special_req =request.form.get("Special_req")
        mycursor.execute('INSERT INTO Table_book (Name, email, Date_time,selected,Special_req) VALUES (%s, %s,%s,%s,%s)', (Name, email, Date_time,selected,Special_req))
        mydb.commit()
    return render_template("booking.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/menu")
def menu():
    return render_template("menu.html")

@app.route("/contact", methods=['POST','GET'])
def contact():
    if request.method=="POST":
        Name=request.form.get("name")
        email = request.form.get("email")
        subject = request.form.get("subject")
        message = request.form.get("message")
        mycursor.execute('INSERT INTO contact (name, email,subject,message) VALUES (%s, %s,%s,%s)', (Name, email,subject,message))
        mydb.commit()
    return render_template("contact.html")

@app.route("/service")
def service():
    return render_template("service.html")
@app.route("/team")
def team():
    return render_template("team.html")
@app.route("/testimonial")
def test():
    return render_template("testimonial.html")

if __name__=="__main__":
    app.run(debug=True)