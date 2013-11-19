from django.conf.urls import patterns, include, url
from django.contrib import admin

from recaptcha.forms import CaptchaLoginForm

admin.autodiscover()
admin.site.login_form = CaptchaLoginForm

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'HNBC.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
