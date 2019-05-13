"""URLS for custom auth"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^singup', views.signup, name='signup'),
    url(r'^search', views.user_list, name='user_search'),

    # APIS
    url(r'^api/v1/users/search',
        views.UsersListView.as_view(),
        name='api_user_search'),
]
