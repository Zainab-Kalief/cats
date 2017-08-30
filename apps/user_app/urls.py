from django.conf.urls import url
from . import views
app_name='user'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^sign_up_test$', views.sign_up_test, name='sign_up_test'),
    url(r'^log_in_test$', views.log_in_test, name='log_in_test'),
]
