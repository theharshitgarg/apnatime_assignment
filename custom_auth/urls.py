from django.conf.urls import url


from . import views


urlpatterns = [
    url(r'^singup', views.signup, name='signup'),

]
