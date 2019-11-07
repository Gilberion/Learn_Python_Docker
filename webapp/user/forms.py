from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"})


class Toolbar(FlaskForm):
    start_cont = SubmitField('start', render_kw={'class': 'btn btn-success'})
    stop_cont = SubmitField('stop', render_kw={'class': 'btn btn-danger'})
    kill_cont = SubmitField('kill', render_kw={'class': 'btn btn-danger'})
    restart_cont = SubmitField('restart', render_kw={'class': 'btn btn-info'})
    pause_cont = SubmitField('pause', render_kw={'class': 'btn btn-info'})
    resume_cont = SubmitField('resume', render_kw={'class': 'btn btn-info'})
    remove_cont = SubmitField('remove', render_kw={'class': 'btn btn-danger'})


class Contadd(FlaskForm):
    cont_name = StringField('Наименование образа', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit_cont_name = SubmitField('create', render_kw={"class": "btn btn-success"})


class Logout(FlaskForm):
    logout = SubmitField('Выйти из панели управления', render_kw={'class': 'btn btn-danger'})
