from django.urls import path
from basic_app import views
from django.conf.urls import url

#template urls
app_name = 'basic_app'

urlpatterns=[
    url(r'^register/$',views.register,name='register'),
    url(r'^login/$',views.user_login,name='user_login'),    
]