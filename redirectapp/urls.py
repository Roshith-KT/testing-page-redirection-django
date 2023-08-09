from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_page, name='redirect_page'),
    path('target/', views.target_page, name='target_page'),
    # Other URL patterns
]
