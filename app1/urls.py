from django.urls import path
from . import views
urlpatterns = [
   path('index/',views.fnIndex,name="index"),
   path('a',views.fnA,name=""),
   path('login/',views.fnLogin,name="login"),
   path('changepassword/',views.fnChangepassword,name="changepassword"),
   path('logins/',views.fnLogins),
   path('test/',views.fntest),
]