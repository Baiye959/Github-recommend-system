import wtforms
from wtforms.validators import Email, Length
from models import UserModel

class RegisterForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="邮箱格式错误")])
    username = wtforms.StringField(validators=[Length(min=3, max=20, message="用户名格式错误")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="密码格式错误")])

    def validate_email(self, field):
        email = field.data
        user = UserModel.query.filter_by(email=email).first()
        if user:
            raise wtforms.ValidationError(message="该邮箱已经被注册")


class LoginForm(wtforms.Form):
    email = wtforms.StringField(validators=[Email(message="邮箱格式错误")])
    password = wtforms.StringField(validators=[Length(min=6, max=20, message="密码格式错误")])