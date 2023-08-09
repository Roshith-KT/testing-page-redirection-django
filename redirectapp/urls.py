from django.urls import path
from . import views

urlpatterns = [
    path('', views.redirect_page, name='redirect_page'),
    # Other URL patterns
]
