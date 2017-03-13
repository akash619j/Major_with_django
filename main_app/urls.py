from django.conf.urls import url
from . import views
urlpatterns=[
  url(r'^$',views.index,name="index"), # we will create index function in views.py it ll return what we want to display
  url(r'^discover/$',views.discover,name="discover"),
  url(r'^discover/video_page/$',views.video_page,name="video_page"),
]