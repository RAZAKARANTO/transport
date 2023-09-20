from flask import Blueprint, render_template
import secrets
#import 

login_bp=Blueprint('login_bp', __name__,template_folder='templates',static_folder='scripts')

@login_bp.route('/login', methods=('GET','POST'))
def loginpage():
    return render_template('login_form.html')