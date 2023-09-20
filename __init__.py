from flask import Flask
from homedir.home_bp_page import home_bp
from logindir.login_bp_page import login_bp

app=Flask(__name__)
app.register_blueprint(home_bp)
app.register_blueprint(login_bp)

