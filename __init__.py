from flask import Flask
from homedir.home_bp_page import home_bp
from logindir.login_bp_page import login_bp


app=Flask(__name__)
app.config['SECRET_KEY']='9ae03f4a506f8e9c9be25cccd0a8d368f2d367bf0e0783f3'
app.register_blueprint(home_bp)
app.register_blueprint(login_bp)

