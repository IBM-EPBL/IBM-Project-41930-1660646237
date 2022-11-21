from flask import render_template,Flask,request,redirect,flash
import ibm_db

import os
conn = ibm_db.connect("")


app = Flask(__name__,template_folder='.')
  
  
@app.route('/')
def helloworld():
    return render_template('index.html')


@app.route('/ventas')
def ventas():
    return render_template('/Home/index.html')


@app.route('/chart')
def chart():
    return render_template('/admin/charts/chartjs.html')


@app.route('/table')
def table():
    students = []
    sql = "SELECT * FROM  LCR86196.Purchase"
    stmt = ibm_db.exec_immediate(conn, sql)
    dictionary = ibm_db.fetch_both(stmt)
    while dictionary != False:
        # print ("The Name is : ",  dictionary)
        students.append(dictionary)
        dictionary = ibm_db.fetch_both(stmt)

    if students:
        return render_template('/admin/tables/basic-table.html', students = students)

@app.route('/ventasSignUp',methods = ['POST', 'GET'])
def ventasSignUp():
  if request.method == 'POST':
    fname = request.form['fname']
    lname = request.form['lname']
    email = request.form['email']
    password = request.form['password']
    phone = request.form['phone']
    insert_sql = "INSERT INTO  LCR86196.VENTAS VALUES(?,?,?,?,?);"
    prep_stmt =ibm_db.prepare(conn, insert_sql)
    ibm_db.bind_param(prep_stmt, 1,fname)
    ibm_db.bind_param(prep_stmt,2, lname)
    ibm_db.bind_param(prep_stmt,3, email)
    ibm_db.bind_param(prep_stmt,4, password)
    ibm_db.bind_param(prep_stmt,5, phone)
        

    account=ibm_db.execute(prep_stmt)
    if account:
        return redirect("/ventas")








@app.route('/orderConfirm',methods = ['POST', 'GET'])
def orderConfirm():
     price=450
     if request.method == 'POST':
        fname = request.form['fname']
        lname = request.form['lname']
        email = request.form['email']
        phone = request.form['phone']
        address1 = request.form['address1']
        address2 = request.form['address2']
        country = request.form['country']
        city = request.form['city']
        state = request.form['state']
        payment = request.form['payment']
        total = price+50
        zipcode = request.form['zipcode']



        insert_sql = "INSERT INTO  LCR86196.Purchase VALUES(?,?,?,?,?,?,?,?,?,?,?,?);"
        prep_stmt =ibm_db.prepare(conn, insert_sql)
        ibm_db.bind_param(prep_stmt, 1,fname)
        ibm_db.bind_param(prep_stmt,2, lname)
        ibm_db.bind_param(prep_stmt,3, email)
        ibm_db.bind_param(prep_stmt,4, phone)
        ibm_db.bind_param(prep_stmt,5,address1)
        ibm_db.bind_param(prep_stmt,6, address2)
        ibm_db.bind_param(prep_stmt,7, country)
        ibm_db.bind_param(prep_stmt,8, city)
        ibm_db.bind_param(prep_stmt,9, state)
        ibm_db.bind_param(prep_stmt,10, zipcode)
        ibm_db.bind_param(prep_stmt,11,payment)
        ibm_db.bind_param(prep_stmt,12,total)
        account=ibm_db.execute(prep_stmt)
        if account:
            return redirect("/ventas")

@app.route('/ventasLogin',methods = ['POST', 'GET'])
def ventasLogin():
  if request.method == 'POST':
    email = request.form['email']
    password = request.form['password']
    insert_sql = "select * from LCR86196.VENTAS where email=? and password=?;"
    prep_stmt =ibm_db.prepare(conn, insert_sql)
    ibm_db.bind_param(prep_stmt, 1, email)
    ibm_db.bind_param(prep_stmt,2, password)
    account=ibm_db.execute(prep_stmt)
    if account:
        return redirect("/ventas")


@app.route('/admin')
def AdminHome():
    return render_template('/admin/adminHome.html')



@app.route('/shop')
def shop():
    return render_template('/Home/shop.html')

@app.route('/detail')
def Detail():
    return render_template('/Home/detail.html')

@app.route('/cart')
def cart():
    return render_template('/Home/cart.html')

@app.route('/checkout')
def checkout():
    return render_template('/Home/checkout.html')

@app.route('/contact')
def contact():
    return render_template('/Home/contact.html')



@app.route('/adminLogincheck',methods = ['POST', 'GET'])
def adminLogincheck():
  if request.method == 'POST':
    email = request.form['email']
    password = request.form['password']
    insert_sql = "select * from admin where email=? and password=?;"
    prep_stmt =ibm_db.prepare(conn, insert_sql)
    ibm_db.bind_param(prep_stmt, 1, email)
    ibm_db.bind_param(prep_stmt,2, password)
    account=ibm_db.execute(prep_stmt)
    if account:
        return redirect("/adminfrontpage")


@app.route('/adminfrontpage')
def adminFrontpage():
        return render_template('/admin/index.html')


@app.route('/adminTable')
def adminTable():
    return render_template('/admin/forms/basic_elements.html')


@app.route('/addProduct',methods = ['POST', 'GET'])
def addProduct():
    if request.method == 'POST':
        id = request.form['id']
        name = request.form['name']
        type = request.form['type']
        price = request.form['price']
        myfile = request.form['myfile']
        seller = request.form['seller']
        insert_sql = "INSERT INTO  LCR86196.PRODUCTS VALUES(?,?,?,?,?,?);"
        prep_stmt =ibm_db.prepare(conn, insert_sql)
        ibm_db.bind_param(prep_stmt, 1, id)
        ibm_db.bind_param(prep_stmt,2, name)
        ibm_db.bind_param(prep_stmt,3, type)
        ibm_db.bind_param(prep_stmt,4, price)
        ibm_db.bind_param(prep_stmt,5, myfile)
        ibm_db.bind_param(prep_stmt,6, seller)
        account=ibm_db.execute(prep_stmt)
    if account:
        return redirect('/adminfrontpage')



if __name__ == '__main__':
     port = int(os.environ.get('PORT', 5000))
     app.run(debug=True, host='0.0.0.0', port=port)