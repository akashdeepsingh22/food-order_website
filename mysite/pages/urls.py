from django.urls import path
from pages import views

urlpatterns = [
    path('', views.index, name='index'),
    path('menu/', views.menu, name='menu'),
    path('order/', views.order, name='order'),
    path('contact/', views.contact, name='contact'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('viewmanu/',views.viewmanu,name='viewmanu'),
    path('menu/<slug:slug>/', views.menu_item_detail, name='menu_item_detail'),
    

]
