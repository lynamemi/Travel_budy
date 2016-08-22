from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name="main"),
    url(r'^travels$', views.travels, name="travels"),
    url(r'^destination/(?P<id>\d+)$', views.destination, name="destination"),
    url(r'^join_trip$', views.join_trip, name="join_trip"),
    url(r'^travels/add$', views.add, name="add"),
    url(r'^add_trip$', views.add_trip, name="add_trip"),
]
# /(?P<id>\d+)$