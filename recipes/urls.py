from django.urls import path
from recipes import views

urlpatterns = [
    path('catalogue/', views.catalogue, name='catalogue'),
    path('create/', views.create_recipe, name='create-recipe'),

]