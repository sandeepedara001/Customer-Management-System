from django.urls import path

from django.http import HttpResponse

from . import views

urlpatterns = [
    path('', views.home, name="home"),

    path('login/', views.loginPage, name="login"),
    path('register/', views.registerPage, name="register"),
    path('logout/', views.logoutUser, name ="logout"),

    path('user/', views.userPage, name="user-page"),

    path('customer/<str:pk_test>/', views.customer, name="customer"),
    path('products/', views.products, name="products"),
    path('create_order/<str:pk>', views.createOrder, name="create_order"),
    path('update_order/<str:pk>', views.updateOrder, name="update_order"),
    path('delete_order/<str:pk>', views.deleteOrder, name="delete_order"),
]
