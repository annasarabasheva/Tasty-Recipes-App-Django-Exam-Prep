from django.urls import path
from profiles import views

urlpatterns = [
    path('create/', views.create_profile, name='create-profile'),
]