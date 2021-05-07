from flask_wtf import FlaskForm
from wtforms import TextField, PasswordField, SubmitField, SelectMultipleField, HiddenField
from flask_pagedown.fields import PageDownField
from wtforms import validators


class LoginForm(FlaskForm):
    username = TextField('Имя*', [validators.Required("Введите имя.")])
    password = PasswordField('Пароль*', [validators.Required("Введите пароль.")])
    submit = SubmitField('Login')


class SignUpForm(FlaskForm):
    username = TextField('Имя*', [validators.Required("Введите имя")])
    email = TextField('Email*', [validators.Required("Введите email"), validators.Email('Некорректный формат Email')])
    password = PasswordField('Пароль*', [validators.Required("Введите пароль"),
                                         validators.EqualTo('confirm_password', message='Пароли должны совпадать')])
    confirm_password = PasswordField('Подтвердить пароль*', [validators.Required("Подтвердите пароль")])
    submit = SubmitField('Signup')


class AddNoteForm(FlaskForm):
    note_id = HiddenField("ID записи:")
    note_title = TextField('Заголовок записи:', [validators.Required("Введите заголовок записи.")])
    note = PageDownField('Ваша запись:')
    tags = SelectMultipleField('Tagи записи:')
    submit = SubmitField('Add Note')


class AddTagForm(FlaskForm):
    tag = TextField('Введите tag:', [validators.Required("Введите tag")])
    submit = SubmitField('Add Tag')


class ChangeEmailForm(FlaskForm):
    email = TextField('Email*', [validators.Required("Введите email"), validators.Email('Некорректный формат Email')])
    submit = SubmitField('Update Email')


class ChangePasswordForm(FlaskForm):
    password = PasswordField('Пароль*', [validators.Required("Введите пароль"),
                                         validators.EqualTo('confirm_password', message='Пароли должны совпадать')])
    confirm_password = PasswordField('Подтверждение пароля*', [validators.Required("Подтвердите пароль")])
    submit = SubmitField('Update Password')
