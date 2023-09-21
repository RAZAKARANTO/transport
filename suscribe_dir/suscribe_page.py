from flask import Blueprint,render_template,request,url_for,redirect, flash
import mariadb

subscribe_bp_page=Blueprint('subscribe_bp_page', __name__, template_folder='templates', static_folder='scripts')

@subscribe_bp_page.route('/subscribe',methods= ('GET', 'POST'))
def subscribe():
    #connection to database
    connection_db=mariadb.connect(
         host='127.0.0.1',
         port= 3306,
         user= 'root',
         password= '603675253674',
         database= 'transport')
    cur= connection_db.cursor()

    if request.method=='POST':
        firstname=request.form['firstname']
        lastname=request.form['lastname']
        username=request.form['username']
        user_password=request.form['password']
        confirm_user_password=request.form['confirm_password']
        cur.execute("SELECT * FROM usersite")
        
    return render_template('suscribe_content.html')