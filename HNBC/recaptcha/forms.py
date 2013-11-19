from captcha.fields import ReCaptchaField

from django.contrib.auth.forms import AuthenticationForm


class CaptchaLoginForm(AuthenticationForm):
      captcha = ReCaptchaField(attrs={'theme' : 'white'})

