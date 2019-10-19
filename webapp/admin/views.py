from flask import render_template, Blueprint
from flask_login import login_required

from webapp.user.forms import Toolbar
from webapp.docker_list import get_list

blueprint = Blueprint('admin', __name__, url_prefix='/admin')

@blueprint.route('/')
@login_required
def admin_index():
    cont_form = Toolbar()
    container_list = get_list()
    return render_template('admin.html', form=cont_form, container_list=container_list)
