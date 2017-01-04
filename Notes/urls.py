from django.conf.urls import url
from django.contrib.auth import views as auth_view
from . import views

app_name ='Notes'

urlpatterns=[

url(r'^$',views.index,name='index'),
url(r'^register/$',views.UserFormView.as_view(),name='register'),
url(r'^note/add/$',views.NoteCreate.as_view(),name="note-add"),
url(r'^note/(?P<pk>[0-9]+)/$',views.NoteUpdate.as_view(),name="note-update"),
url(r'^note/(?P<pk>[0-9]+)/delete/$',views.NoteDelete.as_view(),name="note-delete"),
#url(r'^listdo/add/$',views.ListDoCreate.as_view(),name="listdo-add"),
url(r'^listdo/add/$',views.AddListdoView.as_view(),name="listdo-add"),
url(r'^listdo/(?P<listdo_id>[0-9]+)/items/$',views.UpdateListdoView,name="listdo-update"),
url(r'^listdo/(?P<pk>[0-9]+)/delete/$',views.ListDoDelete.as_view(),name="listdo-delete"),
#url(r'^tag/add/$',views.TagCreate.as_view(),name="tag-add"),
#url(r'^tag/$', views.TagView.as_view(), name="tagview"),
#url(r'^tag/add/$',views.AddUserTagView.as_view(),name="tag-add"),
url(r'^login/$',auth_view.login,name='login'),
url(r'^logout/$',views.logout_page,name='logout'),
url(r'^main_page/$',views.main_page,name='main_page'),
]