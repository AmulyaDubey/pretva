from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('dashboard/<str:pk>', views.dashboard, name="dashboard")
]