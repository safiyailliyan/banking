from . import views
from django.urls import path


urlpatterns = [

    path('register',views.register,name='register'),
    path('register1',views.register1,name='register1'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('form',views.form,name='form'),
    path('application_form',views.application,name='application_form')
]