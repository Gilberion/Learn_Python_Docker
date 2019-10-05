from flask import Flask, render_template, request
from webapp.model import db, login_manager
from flask_login import LoginManager, UserMixin, login_required

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'login'

    @app.route('/')
    def index():
        return render_template('login.html')

        def login():
            message = ''
            if request.method == 'POST':
                username = request.form.get('username')
                password = request.form.get('password')

                if username == 'root' and password == 'pass':
                    message = "Correct username and password"
                else:
                    message = "Wrong username or password"

            return render_template('index.html', message=message)

    @app.route('/admin/')
    @login_required
    def admin():
        return render_template('admin.html')

    return app



