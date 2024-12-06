from django.urls import path, include

from . import views

urlpatterns = [
    path('price/<str:stock_code>/', views.price, name='price'),
    path('correlations/<str:stock_code1>/<str:stock_code2>', views.correlations, name='correlations'),
]