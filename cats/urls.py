from django.conf.urls import url, include

urlpatterns = [
    url(r'^', include('apps.user_app.urls', namespace='user')),
    url(r'^cat/', include('apps.cat_app.urls', namespace='cat')),
]
