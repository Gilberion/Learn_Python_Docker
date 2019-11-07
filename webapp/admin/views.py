from flask import render_template, Blueprint, request, redirect, url_for, flash
from flask_login import login_required

from webapp.user.forms import Toolbar, Logout, Contadd
from webapp.docker_func import get_list, client

import docker
from pywintypes import error as pywintypes_err

blueprint = Blueprint('admin', __name__, url_prefix='/admin')

@blueprint.route('/')
@login_required
def admin_index():
    cont_form = Toolbar()
    logout = Logout()
    contadd =  Contadd()

    try:
        container_list = get_list()

        return render_template(
            'admin.html',
            toolbar_form=cont_form,
            logout_form=logout,
            container_list=container_list,
            contadd_form=contadd
        )
    except pywintypes_err:
        return render_template(
            'error.html',
            warning='Docker is offline. Please run it.'
        )


@blueprint.route('/conteiner_proc', methods=["POST"])
@login_required
def conteiner_proc():
    cont_id = request.form['container_id']
    cont_action = request.form['container_action']

    if cont_action == 'start':
        container = client.containers.get(cont_id)
        container.start()
        return redirect(url_for('admin.admin_index'))
    elif cont_action == 'stop':
        container = client.containers.get(cont_id)
        container.stop()
        return redirect(url_for('admin.admin_index'))
    elif cont_action == 'kill':
        container = client.containers.get(cont_id)
        container.kill()
        return redirect(url_for('admin.admin_index'))
    elif cont_action == 'restart':
        container = client.containers.get(cont_id)
        container.restart()
        return redirect(url_for('admin.admin_index'))
    elif cont_action == 'pause':
        container = client.containers.get(cont_id)
        container.pause()
        return redirect(url_for('admin.admin_index'))
    elif cont_action == 'resume':
        container = client.containers.get(cont_id)
        container.restart()
        return redirect(url_for('admin.admin_index'))
    elif cont_action == 'remove':
        container = client.containers.get(cont_id)
        container.remove()
        return redirect(url_for('admin.admin_index'))

@blueprint.route('/conteiner_add', methods=["POST"])
@login_required
def conteiner_add():
    name = request.form['cont_name']
    try:
        client.containers.run(name)
        return redirect(url_for('admin.admin_index'))
    except docker.errors.ImageNotFound:
        flash('Такого контейнера не существует')
        return redirect(url_for('admin.admin_index'))

        
