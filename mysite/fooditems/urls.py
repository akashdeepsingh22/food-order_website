from django.urls import path
from django.conf.urls.static import static
from fooditems import views
from . import views
from django.conf import settings

urlpatterns = [
    path('manu/', views.manu, name='manu'),
    path('buy_items/', views.buy_items, name='buy_items'),
    path('order_success', views.order_success, name='order_success'),
    path('search/', views.search_items, name='search_items'),
    path('order/', views.place_order, name='place_order'),
    path('selectsuccess/',views.selectsuccess,name='selectsuccess')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)