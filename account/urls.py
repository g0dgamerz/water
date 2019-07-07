from django.urls import path
from . import views

urlpatterns = [
    path('register',views.signup,name='register'),
    path('login',views.logins,name='login'),
    path('activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/', views.activate, name='activate'),
    path('logout',views.logout,name='logout'),
]
