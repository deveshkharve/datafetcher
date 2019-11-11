import config as CONFIG
from flask_cors import CORS
from flask import Flask, render_template, redirect, url_for, request, flash
from flask_assets import Environment, Bundle
from src.auth import auth
from src import fetchService
from utils import utilFunctions

app = Flask(__name__)
assets = Environment(app)
assets.url = app.static_url_path
scss = Bundle('style.scss', filters='pyscss', output='all.css')
assets.register('scss_all', scss)
CORS(app)

DEBUG = False if CONFIG.ENVIRONMENT.lower() == 'production' else True


app.secret_key = 'thisissuperseceret'

# app.register_blueprint(v1, url_prefix='/api/v1')


@app.route("/", methods=['GET', 'POST'])
def home():
    if request.method == 'GET':
        if utilFunctions.hasSession():
            return render_template('home.html')
        else:
            return render_template('login.html')
    elif request.method == 'POST':
        if utilFunctions.hasSession():
            reqJson = request.values
            status, data = fetchService.fetchUrl(**reqJson)
            return render_template('data.html', data=data, status=status, url=reqJson['link'])


@app.route("/logout", methods=['GET', 'POST'])
def logout():
    utilFunctions.deleteSession()
    return redirect(url_for('login'))

@app.route("/login", methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        if utilFunctions.hasSession():
            return redirect(url_for('home'))
        return render_template('login.html')

    elif request.method == 'POST':

        redirectUrl = ''
        reqJson = request.values
        user = auth.validateUser(**reqJson)

        if user:
            utilFunctions.makeSession(user)
            return redirect(url_for('home'))

        flash('Username or password incorrect')

        return render_template('login.html')



if __name__ == "__main__":
    app.run(CONFIG.HOST, CONFIG.PORT, debug=DEBUG)