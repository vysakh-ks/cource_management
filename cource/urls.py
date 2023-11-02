from django.urls import path

from .import views

app_name = 'cource'

urlpatterns = [
    path('',views.home,name="home"),
    path('index/',views.index,name="index"),
    path('register/',views.register,name="register"),
    path('register_data/',views.register_data,name="register_data"),
    path('login_data/',views.login_data,name="login_data"),
    path('home/',views.home,name="home"),
    path('logout_user/',views.logout_user,name="logout_user"),
    path('add_cource/',views.add_cource,name="add_cource"),
    path('cource_data/',views.cource_data,name="cource_data"),
    path('search/',views.search,name="search"),
    path('update_cource/',views.update_cource,name="update_cource"),
    path('update_value/<int:id>/',views.update_value,name="update_value"),
    path('delete_cource/<int:id>/',views.delete_cource,name="delete_cource"),


]