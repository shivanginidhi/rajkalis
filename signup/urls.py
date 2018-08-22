from django.conf.urls import url
from . import views

app_name = 'signup'

urlpatterns = [
    # music/
    url(r'^$', views.IndexView.as_view(), name='index'),
    # music/1/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='details'),
    # signup/album/add
    url(r'^album/add/$', views.CreateView.as_view(), name='album-add'),



]
