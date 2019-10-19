from flask import Flask, render_template, redirect, url_for
from flask_login import LoginManager, current_user, login_required

from webapp.user.forms import Toolbar
from webapp.model import db
from webapp.user.models import User
from webapp.user.views import blueprint as user_blueprint
from webapp.docker_list import get_list

def create_app():
    app = Flask(__name__)
    app.config.from_pyfile('config.py')
    db.init_app(app)

    login_manager = LoginManager()
    login_manager.init_app(app)
    login_manager.login_view = 'user.login'
    app.register_blueprint(user_blueprint)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(user_id)

    @app.route('/')
    def index():
        if current_user.is_authenticated:
            return redirect(url_for('admin_index'))
        else:
            return redirect(url_for('user.login'))

    @app.route('/admin')
    @login_required
    def admin_index():
        cont_form = Toolbar()
        container_list = get_list()
        return render_template('admin.html', form=cont_form, container_list=container_list)

    return app
