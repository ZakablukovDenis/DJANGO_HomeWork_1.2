from django.urls import path, include
from . import views

urlpatterns = [
    # здесь зарегистрируйте вашу view-функцию
    path('', views.homepage),
    path('<recipe>/', views.recipes),
]
