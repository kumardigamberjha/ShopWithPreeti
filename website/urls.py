from django.urls import path

from website import views

urlpatterns = [
    path('', views.Index, name="index"),
    path('ProductView/<str:catname>/', views.ProductView, name="prodview"),
]