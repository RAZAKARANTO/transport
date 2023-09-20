from flask import Blueprint, render_template

login_bp=Blueprint('login_bp', __name__,template_folder='templates',static_folder='scripts')

@login_bp.route('/login')
def loginpage():
    return render_template('login_base.html')