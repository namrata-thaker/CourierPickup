from django.urls import include,path
from . import views

app_name = 'accounts'

urlpatterns =[
    path('pickup/',include('pickup.urls')),
    path('signup/',views.signup_view,name='signup'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),
    path('homepage/',views.homepage,name='homepage'),
    path('',views.index,name='index'),
]