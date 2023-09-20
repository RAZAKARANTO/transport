from flask import Blueprint, render_template,request, url_for, redirect, flash
import secrets
#import 

login_bp=Blueprint('login_bp', __name__,template_folder='templates',static_folder='scripts')

@login_bp.route('/login', methods=('GET','POST'))
def loginpage():
    if request.method=='POST':
        login_name= request.form['login']
        password= request.form['password']
        print("login: "+login_name+", passwrod: "+password )
    return render_template('login_form.html')