from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Имя пользователя', validators=[DataRequired()], render_kw={"class": "form-control"})
    password = PasswordField('Пароль', validators=[DataRequired()], render_kw={"class": "form-control"})
    submit = SubmitField('Отправить', render_kw={"class": "btn btn-primary"})


class Toolbar(FlaskForm):
    start_cont = SubmitField('start', render_kw={'class': 'btn btn-outline-success'})
    stop_cont = SubmitField('stop', render_kw={'class': 'btn btn-outline-danger'})
    kill_cont = SubmitField('kill', render_kw={'class': 'btn btn-outline-danger'})
    restart_cont = SubmitField('restart', render_kw={'class': 'btn btn-outline-info'})
    pause_cont = SubmitField('pause', render_kw={'class': 'btn btn-outline-info'})
    resume_cont = SubmitField('resume', render_kw={'class': 'btn btn-outline-info'})
    remove_cont = SubmitField('remove', render_kw={'class': 'btn btn-outline-danger'})


class Logout(FlaskForm):
    logout = SubmitField('Выйти из панели управления', render_kw={'class': 'btn btn-outline-danger'})
