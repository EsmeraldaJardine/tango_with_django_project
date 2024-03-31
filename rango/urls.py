from django.urls import path
from rango import views

# This code imports the relevant Django machinery for URL mappings and the views
# module from rango. This allows us to call the function url and point to the index
# view for the mapping in urlpatterns.

app_name = 'rango'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('category/<slug:category_name_slug>/', 
         views.show_category, name='show_category'),
    path('add_category/', views.add_category, name='add_category'),
    path('category/<slug:category_name_slug>/add_page/', views.add_page, name='add_page'),
    path('register/', views.register, name='register'),]
