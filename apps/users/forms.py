from django import forms
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    username = forms.CharField(required=True,error_messages={"required":u"用户名必须不能为是空"})
    # password = forms.CharField(required=True, min_length=6,max_length=16,error_messages={"min_length":u"密码不能小于6个","max_length":u"密码不能大于16个"})
    password = forms.RegexField(regex=r'^[A-Za-z][A-Za-z0-9_.]*$',min_length=6,max_length=16,error_messages={"invalid":u'请输入6到16位字母数字下划线'})

class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    # password = forms.CharField(required=True, min_length=5)
    password = forms.RegexField(regex='^[A-Za-z][A-Za-z0-9_.]*$', error_messages={"regex": '只能是字符数字下划线'})
    captcha = CaptchaField(error_messages={"invalid":u"验证码错误"})