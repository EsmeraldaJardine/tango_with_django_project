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
         views.show_category, name='show_category'),]
'''
In Django's URL routing system, the angle brackets `<` and `>` are used 
to define a variable part of the URL that will be captured and passed to 
the view.The syntax inside the angle brackets defines a "path converter"
 and a variable name:
- The part before the colon (`:`) is the path converter. Django provides 
    several built-in path converters, such as `str`, `int`, `slug`, etc. 
- The part after the colon is the variable name. This is the name that will 
    be used in the view to access the captured value. The captured value will
      be passed to the view as a keyword argument with this name.
'''