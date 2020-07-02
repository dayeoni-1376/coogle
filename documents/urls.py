from django.urls import path
from . import views


app_name = 'documents'

urlpatterns = [
    path('search/', views.search, name='search'),
    path('result/', views.result, name='result'),
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    # path('result/', views.model_form_upload, name = "uploaded"),
    # path('signup/', views.signup, name='signup'), # User [C]reate
    # path('login/', views.login, name='login'), # Session [C]reate
    # path('logout/', views.logout, name='logout'), # Session [D]elete
    # path('delete/', views.delete, name='delete'), # User [D]elete
    # path('edit/', views.edit, name='edit'), # User [U]pdate
    # path('password/', views.password, name='password'), # (Password) [U]pdate
    # path('<str:username>/', views.profile, name='profile'),
]
