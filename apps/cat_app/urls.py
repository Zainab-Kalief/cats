from django.conf.urls import url
from . import views
app_name='cat'

urlpatterns = [
    url(r'^home$', views.home, name='home'),
    url(r'^add_cat$', views.add_cat, name='add_cat'),
    url(r'^post_cat$', views.post_cat, name='post_cat'),
    url(r'^post_like/(?P<cat_id>\d+)$', views.add_like, name='add_like'),
    url(r'^delete_cat/(?P<cat_id>\d+)$', views.delete_cat, name='delete_cat'),
    url(r'^edit/(?P<cat_id>\d+)$', views.edit_cat_page, name='edit'),
    url(r'^edit_cat/(?P<cat_id>\d+)$', views.edit_cat, name='edit_cat'),
    url(r'^show_cat/(?P<cat_id>\d+)$', views.show_cat, name='show_cat'),
    url(r'^log_out$', views.log_out, name='log_out'),
]
