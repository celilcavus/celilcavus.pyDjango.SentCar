from django.urls import path

from accountant import views


urlpatterns = [
    path('admin_login',views.adminLogin,name="admin_login"),
    path('admin_logout',views.adminLogout,name="admin_logout"),
    path('register',views.register,name="register"),
]
