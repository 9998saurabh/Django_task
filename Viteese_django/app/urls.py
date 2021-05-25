from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('emailcheck/',views.emailcheck,name='emailcheck'),
    path('register/',views.register_,name = 'register_'),
    path('login/',views.login,name = 'login'),
    path('profileview/',views.Registerd_details,name = 'Registerd_details'),
    path('profileview/saveprofile/',views.saveProfile,name= "saveProfile"),
    path('editprofile/',views.editprofile,name = 'editprofile'),
    path('logoutuser/',views.Logoutuser,name= 'Logoutuser'),
    path('adminpage/',views.admin,name='admin'),

]