from django.urls import path

from menu import views

urlpatterns = [
    path('<str:menu_name>/', views.main_view, name='main_page'),
]