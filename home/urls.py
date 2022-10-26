from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
path("",views.index,name="home"),
path("log_out",views.log_out,name="log_out"),
path("login",views.login_user,name="login_user"),
path("login_user_form",views.login_form,name="login_form"),
path("signup",views.create_user,name="create"),
path("create_user_form",views.create_user_form,name="create_form"),
]
