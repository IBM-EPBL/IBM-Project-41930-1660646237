import email
from turtle import st
from flask import Flask, render_template, request, redirect, url_for, session
from markupsafe import escape

import ibm_db
conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=19af6446-6171-4641-8aba-9dcff8e1b6ff.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=30699;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=lcr86196;PWD=K1KuSfq9rUF9R3C2",'','')

app = Flask(__name__)



@app.route('/')
def home():
  return render_template('home.html')

@app.route('/addstudent')
def new_student():
  return render_template('add_student.html')

@app.route('/login')
def login_student():
  return render_template('login.html')

@app.route('/addrec',methods = ['POST', 'GET'])
def addrec():
  if request.method == 'POST':

    email = request.form['email']
    username = request.form['username']
    rollnumber = request.form['rollnumber']
    password = request.form['password']
    insert_sql = "INSERT INTO students VALUES (?,?,?,?)"
    prep_stmt = ibm_db.prepare(conn, insert_sql)
    ibm_db.bind_param(prep_stmt, 1, email)
    ibm_db.bind_param(prep_stmt, 2, username)
    ibm_db.bind_param(prep_stmt, 3, rollnumber)
    ibm_db.bind_param(prep_stmt, 4, password)
    ibm_db.execute(prep_stmt)
    
    return render_template('signupcomplete.html', msg="Student Data saved successfuly..")


@app.route('/checklogin',methods=['POST'])
def checklogin():
  if request.method=='POST':
    
    email = request.form['email']
    password = request.form['password']

    sql = "SELECT * FROM students WHERE email =? and password=?"
    stmt = ibm_db.prepare(conn, sql)
    ibm_db.bind_param(stmt,1,email)
    ibm_db.bind_param(stmt,2,password)
    ibm_db.execute(stmt)
    account = ibm_db.fetch_assoc(stmt)
    print(account)
    if account:
      return list()
    
@app.route('/signup')
def signup():
  return render_template("signup.html")

@app.route('/list')
def list():
  students = []
  sql = "SELECT * FROM Students"
  stmt = ibm_db.exec_immediate(conn, sql)
  dictionary = ibm_db.fetch_both(stmt)
  while dictionary != False:
    # print ("The Name is : ",  dictionary)
    students.append(dictionary)
    dictionary = ibm_db.fetch_both(stmt)

  if students:
    return render_template("list.html", students = students)
