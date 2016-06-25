from django.conf.urls import url
from django.contrib.auth import views as auth_view
from . import views

app_name ='Notes'

urlpatterns=[

url(r'^$',views.index,name='index'),
url(r'^login/$',auth_view.login,name='login'),
url(r'^logout/$',views.logout_page,name='logout'),
url(r'^main_page/$',views.main_page,name='main_page'),

]