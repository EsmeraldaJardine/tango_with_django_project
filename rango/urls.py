from django.urls import path
from rango import views

# This code imports the relevant Django machinery for URL mappings and the views
# module from rango. This allows us to call the function url and point to the index
# view for the mapping in urlpatterns.

app_name = 'rango'
urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about')
]

# This line defines a URL pattern using the path function. 
# It states that when the root URL (empty string '') is accessed, the index 
# function from the views module should be called. 
# The third and optional parameter is called name. It
# provides a convenient way to reference the view, and by naming our URL mappings
# we can employ reverse URL matching