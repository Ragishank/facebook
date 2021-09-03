from django.urls import path
from . import views
urlpatterns = [
   path('index/',views.fnIndex,name="index"),
   path('a',views.fnA,name=""),
   path('login/',views.fnLogin,name="login"),
   path('changepassword/',views.fnChangepassword,name="changepassword"),
   path('logins/',views.fnLogins),
   path('test/',views.fntest,name='test'),
   path('ajaxex/',views.fnAjax,name='ajaxex'),
   path('add_ajax/',views.fnadd_Ajax,name='add_ajax'),
   path('logout/',views.fnLogout,name='logout'),
   path('edit/',views.fnEdit,name='edit')
]