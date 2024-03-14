from django.shortcuts import render
from django.http import HttpResponse

# view functions are request handlers
# Create your views here.
# With the view created, you’re only part of the way to allowing a user to access it. For
# a user to see your view, you must map a Uniform Resource Locator (URL)⁹ to the view

def index(request):
    about_link = "<a href='/rango/about/'>About</a>"
    return HttpResponse(f"Rango says hey there partner!{about_link}")
# The f at the beginning of the string indicates that it is an f-string, 
# and the expressions inside the curly braces will be evaluated and 
# formatted at runtime.


def about(request):
    index_link = "<a href='/rango/'>Index</a>"
    return HttpResponse(f"Rango says here is the about page. {index_link}")
