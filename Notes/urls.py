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
url(r'^note/search/$',views.NoteSearch,name="search-titles"),
#url(r'^listdo/add/$',views.ListDoCreate.as_view(),name="listdo-add"),
url(r'^listdo/add/$',views.AddListdoView.as_view(),name="listdo-add"),
url(r'^listdo/(?P<listdo_id>[0-9]+)/items/$',views.UpdateListdoView,name="listdo-update"),
url(r'^listdo/(?P<pk>[0-9]+)/delete/$',views.ListDoDelete.as_view(),name="listdo-delete"),
url(r'^tag/add/$',views.TagCreate.as_view(),name="tag-add"),
url(r'^tag/$', views.TagView.as_view(), name="tag-view"),
url(r'^tag/(?P<pk>[0-9]+)/$', views.TagUpdate.as_view(), name="tag-update"),
url(r'^tag/(?P<pk>[0-9]+)/delete/$', views.TagDelete.as_view(), name="tag-delete"),
url(r'^note/tag/add/(?P<pk>[0-9]+)/$',views.NoteTagCreate,name="notetag-create"),
url(r'^note/tag/(?P<pk>[0-9]+)/delete/$',views.NoteTagDelete.as_view(),name="notetag-delete"),
url(r'^listdo/tag/add/(?P<pk>[0-9]+)/$',views.ListDoTagCreate,name="listdotag-create"),
url(r'^listdo/tag/(?P<pk>[0-9]+)/delete/$',views.ListDoTagDelete.as_view(),name="listdotag-delete"),
#ListDoTagCreate
#url(r'^tag/add/$',views.AddUserTagView.as_view(),name="tag-add"),
url(r'^login/$',auth_view.login,name='login'),
url(r'^logout/$',views.logout_page,name='logout'),
url(r'^main_page/$',views.main_page,name='main_page'),
]