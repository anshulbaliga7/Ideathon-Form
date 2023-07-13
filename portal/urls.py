from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from django.urls import path, include,re_path
from . import views


urlpatterns = [
    path('', views.query, name="query"),
    path('logincheck', views.login, name='login'),
    path('new_user/', views.new_user_page, name='new_user_page'),
    path('new_user/newusercheck',views.newusercheck, name='newusercheck'),
    path('loginpage',views.loginpage,name='loginpage'),
    path('new_user/logincheck', views.login, name='login'),
    path('loginpage', views.query1, name="query1"),
    path('submission', views.personal_inf, name='personal_inf'),
    path('new_user/submission', views.personal_inf, name='personal_inf'),
    path('save-member-details/', views.save_member_details, name='save_member_details'),

    path('submitted_form/<int:form_SL>/', views.submitted_form, name='submitted_form'),
    
    path('submit_form_login/', views.submit_form_login, name='submit_form_login'),
    path('submit_form_login/logincheck', views.login, name='login'),
    path('signout', views.loginpage, name='loginpage'),
    path('view_form_users', views.view_form_users, name='view_form_users'),
    path('formcheck', views.formcheck, name='formcheck'),

]

