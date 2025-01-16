from django.urls import path
from django.conf.urls.static import static
from fooditems import views
from . import views
from django.conf import settings

urlpatterns = [
    path('manu/', views.manu, name='manu'),
    path('buy_items/', views.buy_items, name='buy_items'),
    path('order-items/', views.order_items, name='order_items'),
    path('search/', views.search_items, name='search_items'),
    path('selectsuccess/',views.selectsuccess,name='selectsuccess'),
    path('profile/', views.profile, name='profile'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)